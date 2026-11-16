import asyncio
import logging
from collections.abc import Awaitable, Callable

import pytest
from aiohttp import web
from aiohttp.test_utils import TestServer

from lijnpy._rest_adapter import DeLijnAPIException, RestAdapter
from lijnpy.kods_client_v1 import KODSClientV1


def run_against(
    routes: list[web.RouteDef],
    test: Callable[[RestAdapter, TestServer], Awaitable[None]],
):
    """Run `test` with an adapter that talks to a local server serving `routes`."""

    async def main():
        app = web.Application()
        app.add_routes(routes)
        async with TestServer(app) as server:
            async with RestAdapter(api_key="secret") as adapter:
                adapter.url = str(server.make_url("/v1"))
                await test(adapter, server)

    asyncio.run(main())


async def ok(_: web.Request) -> web.Response:
    return web.json_response({"answer": 42})


def test_get_returns_data():
    async def test(adapter: RestAdapter, _):
        result = await adapter.get("/ok")
        assert result.status_code == 200
        assert result.data == {"answer": 42}

    run_against([web.get("/v1/ok", ok)], test)


def test_api_key_and_params_are_sent():
    async def echo(request: web.Request) -> web.Response:
        return web.json_response(
            {"key": request.headers["Ocp-Apim-Subscription-Key"], **request.query}
        )

    async def test(adapter: RestAdapter, _):
        result = await adapter.get("/echo", {"a": "1"})
        assert result.data == {"key": "secret", "a": "1"}

    run_against([web.get("/v1/echo", echo)], test)


def test_post_and_delete_send_a_body():
    async def echo_body(request: web.Request) -> web.Response:
        return web.json_response(
            {"method": request.method, "body": await request.json()}
        )

    async def test(adapter: RestAdapter, _):
        post = await adapter.post("/echo", data={"x": 1})
        assert post.data == {"method": "POST", "body": {"x": 1}}
        delete = await adapter.delete("/echo", data={"y": 2})
        assert delete.data == {"method": "DELETE", "body": {"y": 2}}

    run_against(
        [web.post("/v1/echo", echo_body), web.delete("/v1/echo", echo_body)], test
    )


def test_not_found_with_non_json_body_mentions_the_status():
    async def not_found(_: web.Request) -> web.Response:
        return web.Response(status=404, text="Resource not found", reason="Not Found")

    async def test(adapter: RestAdapter, _):
        with pytest.raises(DeLijnAPIException, match="404: Not Found"):
            await adapter.get("/berichten")

    run_against([web.get("/v1/berichten", not_found)], test)


def test_server_error_with_json_body_mentions_the_status():
    async def broken(_: web.Request) -> web.Response:
        return web.json_response({"error": "boom"}, status=500)

    async def test(adapter: RestAdapter, _):
        with pytest.raises(DeLijnAPIException, match="500"):
            await adapter.get("/broken")

    run_against([web.get("/v1/broken", broken)], test)


def test_bad_json_in_a_successful_response():
    async def not_json(_: web.Request) -> web.Response:
        return web.Response(text="<html>oops</html>", content_type="text/html")

    async def test(adapter: RestAdapter, _):
        with pytest.raises(DeLijnAPIException, match="Bad JSON"):
            await adapter.get("/html")

    run_against([web.get("/v1/html", not_json)], test)


def test_connection_error():
    async def main():
        async with RestAdapter() as adapter:
            adapter.url = "http://127.0.0.1:1/v1"  # nothing listens on port 1
            with pytest.raises(DeLijnAPIException, match="Request failed"):
                await adapter.get("/ok")

    asyncio.run(main())


def test_errors_are_logged(caplog: pytest.LogCaptureFixture):
    async def not_found(_: web.Request) -> web.Response:
        return web.Response(status=404)

    async def test(adapter: RestAdapter, _):
        with pytest.raises(DeLijnAPIException):
            await adapter.get("/missing")

    with caplog.at_level(logging.ERROR):
        run_against([web.get("/v1/missing", not_found)], test)
    assert "status_code=404" in caplog.text


def test_session_is_reused_and_can_be_closed():
    async def test(adapter: RestAdapter, _):
        await adapter.get("/ok")
        session = adapter._session
        assert session is not None
        await adapter.get("/ok")
        assert adapter._session is session
        await adapter.close()
        assert session.closed
        await adapter.close()  # closing twice is fine
        # A closed adapter opens a fresh session when used again
        await adapter.get("/ok")
        assert adapter._session is not session

    run_against([web.get("/v1/ok", ok)], test)


def test_client_close_closes_the_session():
    async def main():
        async with KODSClientV1() as client:
            session = client.http_client._get_session()  # type: ignore[attr-defined]
        assert session.closed

    asyncio.run(main())
