import asyncio
import json
from datetime import date, datetime, timezone
from pathlib import Path
from unittest.mock import Mock

import pytest
from aiohttp import web
from aiohttp.test_utils import TestServer
from pydantic_extra_types.coordinate import Latitude, Longitude

from lijnpy.enums import LineDirection
from lijnpy._query import format_bool, format_date, format_datetime, format_int
from lijnpy._rest_adapter import RestAdapter, Result
from lijnpy.kods_client_v1 import KODSClientV1
from lijnpy.models import GeoCoordinate

FIXTURES = Path("tests/inputs/kods_client/v1")
MOMENT = datetime(2026, 11, 20, 8, 5, 9)
LINE_DIRECTIONS = [(1, 22, LineDirection.TO), (1, 22, LineDirection.FROM)]
LOCATION = GeoCoordinate(latitude=Latitude(51.2194), longitude=Longitude(4.4025))


def test_format_datetime():
    assert format_datetime(MOMENT) == "2026-11-20T08:05:09"
    assert format_datetime(datetime(2026, 1, 2, 3, 4, 5, 999)) == "2026-01-02T03:04:05"
    assert format_datetime(date(2026, 11, 20)) == "2026-11-20T00:00:00"
    assert format_datetime(None) is None


def test_format_datetime_rejects_a_time_zone():
    with pytest.raises(ValueError, match="naive"):
        format_datetime(datetime(2026, 11, 20, 8, tzinfo=timezone.utc))


def test_format_date():
    assert format_date(date(2026, 11, 20)) == "2026-11-20"
    assert format_date(MOMENT) == "2026-11-20"
    assert format_date(None) is None


def test_format_bool_and_int():
    assert format_bool(True) == "true"
    assert format_bool(False) == "false"
    assert format_bool(None) is None
    assert format_int(50) == "50"
    assert format_int(None) is None


def recording_client(
    fixture: str,
) -> tuple[KODSClientV1, list[tuple[str, dict | None]]]:
    """A client that records (path, query parameters) and answers with a fixture."""
    calls: list[tuple[str, dict | None]] = []
    data = json.loads((FIXTURES / f"{fixture}.json").read_text())

    async def get(path: str, ep_params: dict | None = None) -> Result:
        calls.append((path, ep_params))
        return Result(status_code=200, data=data)

    return KODSClientV1(http_client=Mock(spec_set=RestAdapter, get=get)), calls


# (fixture, call, expected path, expected query parameters)
CASES = [
    (
        "stops_by_entity",
        lambda c: c.get_stops_by_entity(1, valid_on=MOMENT),
        "/entiteiten/1/haltes",
        {"geldigOp": "2026-11-20T08:05:09"},
    ),
    (
        "lines_by_entity",
        lambda c: c.get_lines_by_entity(1, valid_on=MOMENT),
        "/entiteiten/1/lijnen",
        {"geldigOp": "2026-11-20T08:05:09"},
    ),
    (
        "stops_by_municipality",
        lambda c: c.get_stops(482, valid_on=date(2026, 11, 20)),
        "/gemeenten/482/haltes",
        {"geldigOp": "2026-11-20T00:00:00"},
    ),
    (
        "lines_by_municipality",
        lambda c: c.get_lines(482, valid_on=MOMENT),
        "/gemeenten/482/lijnen",
        {"geldigOp": "2026-11-20T08:05:09"},
    ),
    (
        "stops_in_vicinity",
        lambda c: c.get_stops_in_vicinity(LOCATION, radius=100, max_stops=3),
        "/haltes/indebuurt/51.2194,4.4025",
        {"radius": "100", "maxAantalHaltes": "3"},
    ),
    (
        "stop",
        lambda c: c.get_stop(1, 102675, valid_on=MOMENT),
        "/haltes/1/102675",
        {"geldigOp": "2026-11-20T08:05:09"},
    ),
    (
        "timetable",
        lambda c: c.get_timetable(
            1, 102675, day=date(2026, 11, 20), include_last_passage=True
        ),
        "/haltes/1/102675/dienstregelingen",
        {"datum": "2026-11-20", "inclusiefLaatsteDoorkomst": "true"},
    ),
    (
        "directions",
        lambda c: c.get_directions(1, 102675, valid_on=MOMENT),
        "/haltes/1/102675/lijnrichtingen",
        {"geldigOp": "2026-11-20T08:05:09"},
    ),
    (
        "detours",
        lambda c: c.get_detours(1, 102675, day=date(2026, 11, 20)),
        "/haltes/1/102675/omleidingen",
        {"datum": "2026-11-20"},
    ),
    (
        "real_time_timetable",
        lambda c: c.get_real_time_timetable(1, 102675, max_passages=2),
        "/haltes/1/102675/real-time",
        {"maxAantalDoorkomsten": "2"},
    ),
    (
        "disruptions",
        lambda c: c.get_disruptions(1, 102675, day=date(2026, 11, 20)),
        "/haltes/1/102675/storingen",
        {"datum": "2026-11-20"},
    ),
    (
        "lines",
        lambda c: c.get_all_lines(valid_on=MOMENT),
        "/lijnen",
        {"geldigOp": "2026-11-20T08:05:09"},
    ),
    (
        "line",
        lambda c: c.get_line(1, 22, valid_on=MOMENT),
        "/lijnen/1/22",
        {"geldigOp": "2026-11-20T08:05:09"},
    ),
    (
        "municipalities_by_line",
        lambda c: c.get_municipalities_by_line(1, 22, valid_on=MOMENT),
        "/lijnen/1/22/gemeenten",
        {"geldigOp": "2026-11-20T08:05:09"},
    ),
    (
        "line_colors",
        lambda c: c.get_line_colors(1, 22, valid_on=MOMENT),
        "/lijnen/1/22/lijnkleuren",
        {"geldigOp": "2026-11-20T08:05:09"},
    ),
    (
        "line_directions",
        lambda c: c.get_line_directions(1, 22, valid_on=MOMENT),
        "/lijnen/1/22/lijnrichtingen",
        {"geldigOp": "2026-11-20T08:05:09"},
    ),
    (
        "line_direction",
        lambda c: c.get_line_direction(1, 22, LineDirection.FROM, valid_on=MOMENT),
        "/lijnen/1/22/lijnrichtingen/TERUG",
        {"geldigOp": "2026-11-20T08:05:09"},
    ),
    (
        "line_direction_timetable",
        lambda c: c.get_line_direction_timetable(
            1, 22, LineDirection.TO, day=date(2026, 11, 20)
        ),
        "/lijnen/1/22/lijnrichtingen/HEEN/dienstregelingen",
        {"datum": "2026-11-20"},
    ),
    (
        "line_direction_ride",
        lambda c: c.get_line_direction_ride(
            1, 22, LineDirection.TO, 3, day=date(2026, 11, 20)
        ),
        "/lijnen/1/22/lijnrichtingen/HEEN/rit/3",
        {"datum": "2026-11-20"},
    ),
    (
        "line_direction_stops",
        lambda c: c.get_line_direction_stops(1, 22, LineDirection.TO, valid_on=MOMENT),
        "/lijnen/1/22/lijnrichtingen/HEEN/haltes",
        {"geldigOp": "2026-11-20T08:05:09"},
    ),
    (
        "line_direction_detours",
        lambda c: c.get_line_direction_detours(
            1, 22, LineDirection.TO, day=date(2026, 11, 20)
        ),
        "/lijnen/1/22/lijnrichtingen/HEEN/omleidingen",
        {"datum": "2026-11-20"},
    ),
    (
        "all_detours",
        lambda c: c.get_all_detours(start=MOMENT, end=date(2026, 11, 27)),
        "/omleidingen",
        {"startDatum": "2026-11-20T08:05:09", "eindDatum": "2026-11-27T00:00:00"},
    ),
    (
        "detours_by_line_directions",
        lambda c: c.get_detours_by_line_directions(
            LINE_DIRECTIONS, day=date(2026, 11, 20)
        ),
        "/lijnen/lijst/1_22_HEEN_1_22_TERUG/omleidingen",
        {"datum": "2026-11-20"},
    ),
    (
        "disruptions_by_line_directions",
        lambda c: c.get_disruptions_by_line_directions(
            LINE_DIRECTIONS, day=date(2026, 11, 20)
        ),
        "/lijnen/lijst/1_22_HEEN_1_22_TERUG/storingen",
        {"datum": "2026-11-20"},
    ),
    (
        "line_direction_disruptions",
        lambda c: c.get_line_direction_disruptions(
            1, 22, LineDirection.TO, day=date(2026, 11, 20)
        ),
        "/lijnen/1/22/lijnrichtingen/HEEN/storingen",
        {"datum": "2026-11-20"},
    ),
]


@pytest.mark.parametrize("fixture, call, path, params", CASES)
def test_parameters_are_sent_formatted(fixture, call, path, params):
    client, calls = recording_client(fixture)
    asyncio.run(call(client))
    assert calls == [(path, params)]


@pytest.mark.parametrize("fixture, call, path, params", CASES)
def test_nothing_is_sent_without_parameters(fixture, call, path, params):
    """Omitted parameters must not change the request: no `None` and no empty query."""
    client, calls = recording_client(fixture)
    # The same call, with every optional argument left out
    bare = {
        "stops_by_entity": lambda c: c.get_stops_by_entity(1),
        "lines_by_entity": lambda c: c.get_lines_by_entity(1),
        "stops_by_municipality": lambda c: c.get_stops(482),
        "lines_by_municipality": lambda c: c.get_lines(482),
        "stops_in_vicinity": lambda c: c.get_stops_in_vicinity(LOCATION),
        "stop": lambda c: c.get_stop(1, 102675),
        "timetable": lambda c: c.get_timetable(1, 102675),
        "directions": lambda c: c.get_directions(1, 102675),
        "detours": lambda c: c.get_detours(1, 102675),
        "real_time_timetable": lambda c: c.get_real_time_timetable(1, 102675),
        "disruptions": lambda c: c.get_disruptions(1, 102675),
        "lines": lambda c: c.get_all_lines(),
        "line": lambda c: c.get_line(1, 22),
        "municipalities_by_line": lambda c: c.get_municipalities_by_line(1, 22),
        "line_colors": lambda c: c.get_line_colors(1, 22),
        "line_directions": lambda c: c.get_line_directions(1, 22),
        "line_direction": lambda c: c.get_line_direction(1, 22, LineDirection.FROM),
        "line_direction_timetable": lambda c: c.get_line_direction_timetable(
            1, 22, LineDirection.TO
        ),
        "line_direction_ride": lambda c: c.get_line_direction_ride(
            1, 22, LineDirection.TO, 3
        ),
        "line_direction_stops": lambda c: c.get_line_direction_stops(
            1, 22, LineDirection.TO
        ),
        "line_direction_detours": lambda c: c.get_line_direction_detours(
            1, 22, LineDirection.TO
        ),
        "line_direction_disruptions": lambda c: c.get_line_direction_disruptions(
            1, 22, LineDirection.TO
        ),
        "all_detours": lambda c: c.get_all_detours(),
        "detours_by_line_directions": lambda c: c.get_detours_by_line_directions(
            LINE_DIRECTIONS
        ),
        "disruptions_by_line_directions": (
            lambda c: c.get_disruptions_by_line_directions(LINE_DIRECTIONS)
        ),
    }[fixture]
    asyncio.run(bare(client))
    assert calls == [(path, None)]


def test_only_the_given_parameters_are_sent():
    client, calls = recording_client("timetable")
    asyncio.run(client.get_timetable(1, 102675, include_last_passage=False))
    assert calls == [
        ("/haltes/1/102675/dienstregelingen", {"inclusiefLaatsteDoorkomst": "false"})
    ]


def test_parameters_reach_the_server_in_the_query_string():
    """End to end through aiohttp, which rejects bool and None query values."""
    seen: list[dict[str, str]] = []

    async def timetable(request: web.Request) -> web.Response:
        seen.append(dict(request.query))
        return web.json_response(json.loads((FIXTURES / "timetable.json").read_text()))

    async def main():
        app = web.Application()
        app.add_routes([web.get("/v1/haltes/1/102675/dienstregelingen", timetable)])
        async with TestServer(app) as server:
            adapter = RestAdapter()
            adapter.url = str(server.make_url("/v1"))
            async with KODSClientV1(http_client=adapter) as client:
                await client.get_timetable(
                    1, 102675, day=date(2026, 11, 20), include_last_passage=True
                )
                await client.get_timetable(1, 102675)

    asyncio.run(main())
    assert seen == [
        {"datum": "2026-11-20", "inclusiefLaatsteDoorkomst": "true"},
        {},
    ]


def test_line_direction_real_time_has_no_query_parameters():
    client, calls = recording_client("line_direction_real_time_timetable")
    asyncio.run(client.get_line_direction_real_time_timetable(1, 22, LineDirection.TO))
    assert calls == [("/lijnen/1/22/lijnrichtingen/HEEN/real-time", None)]


def test_line_direction_lists_need_at_least_one_line_direction():
    client, calls = recording_client("detours_by_line_directions")
    with pytest.raises(ValueError, match="at least one"):
        asyncio.run(client.get_detours_by_line_directions([]))
    assert calls == []
