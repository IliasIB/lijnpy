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

client = KODSClientV1(
    api_key=get_api_key() or "", logger=logging.getLogger("live-test")
)
calls = get_calls(client)


@pytest.mark.parametrize("method", calls)
def test_endpoint(method: str):
    _, call = calls[method]
    assert asyncio.run(call()) is not None
