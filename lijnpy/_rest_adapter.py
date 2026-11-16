from __future__ import annotations

from logging import Logger, getLogger
from typing import Any

import aiohttp
from pydantic import BaseModel


class Result(BaseModel):
    """The result of a request to the De Lijn API

    Attributes:
        status_code (int): The status code of the request
        message (str, optional): The message of the request. Defaults to "".
        data (dict[str, Any] | None, optional): The data of the request. Defaults to None.
    """

    status_code: int
    message: str = ""
    data: dict[str, Any] | None = None


class DeLijnAPIException(Exception): ...


class RestAdapter:
    def __init__(
        self,
        hostname: str = "api.delijn.be",
        api_key: str = "",
        ver: str = "v1",
        ssl_verify: bool = True,
        logger: Logger | None = None,
    ):
        """
        Constructor for RestAdapter

        Args:
            hostname (str, optional): The hostname of the API. Defaults to "api.delijn.be".
            api_key (str, optional): The API key to use for authentication. Defaults to "".
            ver (str, optional): The version of the API to use. Defaults to "v1".
            ssl_verify (bool, optional): Whether to verify the SSL certificate. Defaults to True.
            logger (Logger | None, optional): The logger to use for logging. Defaults to None.
        """
        self.url = f"https://{hostname}/{ver}"
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        self._logger = logger or getLogger(__name__)
        self._session: aiohttp.ClientSession | None = None

    def _get_session(self) -> aiohttp.ClientSession:
        """Return the shared session, creating it on first use (or after close)"""
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def close(self) -> None:
        """Close the underlying HTTP session. Safe to call more than once."""
        if self._session is not None:
            await self._session.close()
            self._session = None

    async def __aenter__(self) -> RestAdapter:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close()

    async def _do(
        self,
        http_method: str,
        endpoint: str,
        ep_params: dict | None = None,
        data: dict | None = None,
    ) -> Result:
        """Perform an HTTP request to the API and return a Result object

        Args:
            http_method (str): The HTTP method to use (GET, POST, DELETE)
            endpoint (str): The endpoint on the API to request
            ep_params (dict | None, optional): Parameters to give to the endpoint. Defaults to None.
            data (dict | None, optional): Data to pass through to the endpoint. Defaults to None.

        Raises:
            DeLijnAPIException: If the request fails or the response is not in the 200-299 range

        Returns:
            Result: The result of the request
        """
        full_url = self.url + endpoint
        headers = {"Ocp-Apim-Subscription-Key": self._api_key}

        log_line_pre = f"method={http_method}, url={full_url}, params={ep_params}"

        def log_line_post(success: bool, status: int | None, message: object) -> str:
            return (
                f"{log_line_pre}, success={success}, "
                f"status_code={status}, message={message}"
            )

        self._logger.debug(msg=log_line_pre)
        try:
            async with self._get_session().request(
                method=http_method,
                url=full_url,
                headers=headers,
                params=ep_params,
                json=data,
            ) as response:
                status = response.status
                reason = response.reason
                # Check the status before the body: error responses are often not JSON
                if not 200 <= status <= 299:
                    self._logger.error(msg=log_line_post(False, status, reason))
                    raise DeLijnAPIException(f"{status}: {reason}")
                try:
                    data_out = await response.json(content_type=None)
                except ValueError as e:  # includes JSONDecodeError
                    self._logger.error(msg=log_line_post(False, status, e))
                    raise DeLijnAPIException(
                        f"Bad JSON in response ({status}: {reason})"
                    ) from e
        except DeLijnAPIException:
            raise
        except (aiohttp.ClientError, TimeoutError) as e:
            self._logger.error(msg=f"{log_line_pre}, error={e!r}")
            raise DeLijnAPIException(f"Request failed: {e!r}") from e

        self._logger.debug(msg=log_line_post(True, status, reason))
        return Result(
            status_code=status, message=reason or "No reason given", data=data_out
        )

    async def get(self, endpoint: str, ep_params: dict | None = None) -> Result:
        """Perform a GET request to the API

        Args:
            endpoint (str): The endpoint on the API to GET
            ep_params (dict | None, optional): Parameters to give to the endpoint. Defaults to None.

        Returns:
            Result: The result of the GET request
        """
        return await self._do(http_method="GET", endpoint=endpoint, ep_params=ep_params)

    async def post(
        self, endpoint: str, ep_params: dict | None = None, data: dict | None = None
    ) -> Result:
        """Perform a POST request to the API

        Args:
            endpoint (str): The endpoint on the API to POST
            ep_params (dict | None, optional): Parameters to give to the endpoint. Defaults to None.
            data (dict | None, optional): Data to pass through to the endpoint. Defaults to None.

        Returns:
            Result: The result of the POST request
        """
        return await self._do(
            http_method="POST", endpoint=endpoint, ep_params=ep_params, data=data
        )

    async def delete(
        self, endpoint: str, ep_params: dict | None = None, data: dict | None = None
    ) -> Result:
        """Perform a DELETE request to the API

        Args:
            endpoint (str): The endpoint on the API to DELETE
            ep_params (dict | None, optional): Parameters to give to the endpoint. Defaults to None.
            data (dict | None, optional): Data to pass through to the endpoint. Defaults to None.

        Returns:
            Result: The result of the DELETE request
        """
        return await self._do(
            http_method="DELETE", endpoint=endpoint, ep_params=ep_params, data=data
        )
