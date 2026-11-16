"""Smoke test against the real De Lijn API.

Calls every client method once and validates the response against the models.
Skipped unless DELIJN_API_KEY is set, and deselected by default (see the
`live` marker in pyproject.toml). Run it with:

    DELIJN_API_KEY=... uv run pytest -m live
"""

import asyncio
import logging

import pytest
from live_calls import API_KEY_VARIABLE, get_api_key, get_calls

from lijnpy.kods_client_v1 import KODSClientV1

pytestmark = [
    pytest.mark.live,
    pytest.mark.skipif(get_api_key() is None, reason=f"{API_KEY_VARIABLE} is not set"),
]



@pytest.mark.parametrize("method", get_calls(KODSClientV1()))
def test_endpoint(method: str):
    async def call():
        # A client (and its session) belongs to one event loop, so make one per test
        async with KODSClientV1(
            api_key=get_api_key() or "", logger=logging.getLogger("live-test")
        ) as client:
            _, make_call = get_calls(client)[method]
            return await make_call()

    assert asyncio.run(call()) is not None
