import asyncio
import json
from pathlib import Path
from typing import cast
from unittest.mock import Mock

import pytest
from pydantic_extra_types.coordinate import Latitude, Longitude

from lijnpy._rest_adapter import DeLijnAPIException, RestAdapter, Result
from lijnpy.enums import Accessibility, Language
from lijnpy.kods_client_v1 import KODSClientV1
from lijnpy.models import GeoCoordinate


def get_async_http_mock(
    status_code: int = 200, message: str = "Success", data: dict = {}
):
    async def async_http_get_mock(_: str):
        return Result(status_code=status_code, message=message, data=data)

    return Mock(spec_set=RestAdapter, get=async_http_get_mock)


def get_client_for_json(path: str):
    with Path(path).open() as file:
        http_client = get_async_http_mock(data=json.load(file))

    return KODSClientV1(http_client=http_client)


def test_colors():
    colors = asyncio.run(
        get_client_for_json("tests/inputs/kods_client/v1/colors.json").get_colors()
    )
    assert len(colors) == 24


def test_colors_empty():
    with pytest.raises(DeLijnAPIException):
        asyncio.run(KODSClientV1(http_client=get_async_http_mock()).get_colors())


def test_color():
    color = asyncio.run(
        get_client_for_json("tests/inputs/kods_client/v1/color.json").get_color("TU")
    )
    assert color.code == "TU"
    assert color.description == "Turkoois"
    assert color.color.as_hex() == "#09a"


def test_entities():
    entities = asyncio.run(
        get_client_for_json("tests/inputs/kods_client/v1/entities.json").get_entities()
    )
    assert len(entities) == 5


def test_entity():
    entity = asyncio.run(
        get_client_for_json("tests/inputs/kods_client/v1/entity.json").get_entity(1)
    )
    assert entity.number == 1
    assert entity.code == "A"
    assert entity.description == "Antwerpen"


def test_municipalities_by_entity():
    municipalities = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/municipalities_by_entity.json"
        ).get_municipalities_by_entity(1)
    )
    assert len(municipalities) == 341


def test_stops_by_entity():
    stops = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/stops_by_entity.json"
        ).get_stops(1)
    )
    assert len(stops) == 6801


def test_lines_by_entity():
    lines = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/lines_by_entity.json"
        ).get_lines(1)
    )
    assert len(lines) == 286


def test_municipalities():
    municipalities = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/municipalities.json"
        ).get_municipalities()
    )
    assert len(municipalities) == 1913


def test_stops():
    stops = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/stops_by_municipality.json"
        ).get_stops(1866)
    )
    assert len(stops) == 417


def test_lines():
    lines_response = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/lines_by_municipality.json"
        ).get_lines(1866)
    )
    assert len(lines_response) == 74


def test_municipality():
    gemeente = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/municipality.json"
        ).get_municipality(1)
    )
    assert gemeente.number == 1491
    assert gemeente.description == "HOUTHALEN"
    assert gemeente.main_municipality is not None
    assert gemeente.main_municipality.number == 1422
    assert gemeente.main_municipality.description == "HOUTHALEN-HELCHTEREN"


def test_stops_in_vicinity():
    stops_in_vicinity = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/stops_in_vicinity.json"
        ).get_stops_in_vicinity(
            GeoCoordinate(
                latitude=cast(Latitude, 51.004652), longitude=cast(Longitude, 5.346613)
            )
        )
    )
    assert len(stops_in_vicinity) == 7


def test_stop():
    stop = asyncio.run(
        get_client_for_json("tests/inputs/kods_client/v1/stop.json").get_stop(4, 408581)
    )
    assert stop.entity_number == 4
    assert stop.number == 408581
    assert stop.description == "Koning Boudewijnlaan"
    assert stop.description_long == "Heverlee Koning Boudewijnlaan"
    assert stop.municipality_number == 1866
    assert stop.municipality_description == "Leuven"
    assert stop.geo_coordinate.latitude == 50.868276
    assert stop.geo_coordinate.longitude == 4.68115
    assert stop.accessibilities == [
        Accessibility.MOTOR_WITH_ASSIST,
        Accessibility.MOTOR_DISABILITY,
    ]
    assert stop.is_main is None
    assert stop.language == Language.UNKNOWN


def test_timetable():
    timetable = asyncio.run(
        get_client_for_json("tests/inputs/kods_client/v1/timetable.json").get_timetable(
            4, 408581
        )
    )
    assert len(timetable.passages) == 2
    assert len(timetable.ride_notes) == 0
    assert len(timetable.passage_notes) == 0
    assert len(timetable.detours) == 0


def test_directions():
    directions = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/directions.json"
        ).get_directions(4, 408581)
    )
    assert len(directions) == 2


def test_detours():
    detours = asyncio.run(
        get_client_for_json("tests/inputs/kods_client/v1/detours.json").get_detours(
            3, 308530
        )
    )
    assert len(detours) == 1


def test_real_time_timetable():
    real_time_timetable = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/real_time_timetable.json"
        ).get_real_time_timetable(4, 403022)
    )
    assert len(real_time_timetable.passages) == 1
    assert len(real_time_timetable.ride_notes) == 0
    assert len(real_time_timetable.passage_notes) == 0
    assert len(real_time_timetable.detours) == 0


def test_disruption():
    disruptions_response = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/disruptions.json"
        ).get_disruptions(4, 403022)
    )
    assert len(disruptions_response) == 1


def test_transport_regions():
    transport_regions = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/transport_regions.json"
        ).get_transport_regions()
    )
    assert len(transport_regions) == 15


def test_transport_region():
    vervoerregio = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/transport_region.json"
        ).get_transport_region("AA")
    )
    assert vervoerregio.code == "AA"
    assert vervoerregio.name == "Aalst"
    assert vervoerregio.number == 1


def test_lines_by_transport_region():
    lines = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/lines_by_transport_region.json"
        ).get_lines_by_transport_region("AN")
    )
    assert len(lines) == 34
