"""Smoke test against the real De Lijn API.

Calls every client method once and validates the response against the models.
Skipped unless DELIJN_API_KEY is set, and deselected by default (see the
`live` marker in pyproject.toml). Run it with:

    DELIJN_API_KEY=... uv run pytest -m live
"""

import asyncio
import logging
from datetime import date, datetime, timedelta

import pytest
from live_calls import (
    API_KEY_VARIABLE,
    DIRECTION,
    ENTITY,
    LINE,
    LOCATION,
    MUNICIPALITY,
    STOP,
    get_api_key,
    get_calls,
)

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


# The same endpoints with their optional query parameters set, to check that the
# API accepts the formats the client sends
PARAMETER_CALLS = {
    "get_stops_by_entity": lambda c: c.get_stops_by_entity(
        ENTITY, valid_on=datetime.now()
    ),
    "get_lines_by_entity": lambda c: c.get_lines_by_entity(
        ENTITY, valid_on=datetime.now()
    ),
    "get_stops": lambda c: c.get_stops(MUNICIPALITY, valid_on=date.today()),
    "get_lines": lambda c: c.get_lines(MUNICIPALITY, valid_on=datetime.now()),
    "get_stops_in_vicinity": lambda c: c.get_stops_in_vicinity(
        LOCATION, radius=500, max_stops=5
    ),
    "get_stop": lambda c: c.get_stop(ENTITY, STOP, valid_on=datetime.now()),
    "get_timetable": lambda c: c.get_timetable(
        ENTITY, STOP, day=date.today() + timedelta(days=1), include_last_passage=True
    ),
    "get_directions": lambda c: c.get_directions(ENTITY, STOP, valid_on=datetime.now()),
    "get_detours": lambda c: c.get_detours(ENTITY, STOP, day=date.today()),
    "get_real_time_timetable": lambda c: c.get_real_time_timetable(
        ENTITY, STOP, max_passages=2
    ),
    "get_disruptions": lambda c: c.get_disruptions(ENTITY, STOP, day=date.today()),
    "get_all_lines": lambda c: c.get_all_lines(valid_on=datetime.now()),
    "get_line": lambda c: c.get_line(ENTITY, LINE, valid_on=datetime.now()),
    "get_municipalities_by_line": lambda c: c.get_municipalities_by_line(
        ENTITY, LINE, valid_on=datetime.now()
    ),
    "get_line_colors": lambda c: c.get_line_colors(
        ENTITY, LINE, valid_on=datetime.now()
    ),
    "get_line_directions": lambda c: c.get_line_directions(
        ENTITY, LINE, valid_on=datetime.now()
    ),
    "get_line_direction": lambda c: c.get_line_direction(
        ENTITY, LINE, DIRECTION, valid_on=datetime.now()
    ),
}


@pytest.mark.parametrize("method", PARAMETER_CALLS)
def test_endpoint_with_parameters(method: str):
    async def call():
        async with KODSClientV1(
            api_key=get_api_key() or "", logger=logging.getLogger("live-test")
        ) as client:
            return await PARAMETER_CALLS[method](client)

    assert asyncio.run(call()) is not None
