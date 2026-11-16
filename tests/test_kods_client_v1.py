import asyncio
import inspect
import json
from pathlib import Path
from typing import cast
from unittest.mock import Mock

import pytest
from pydantic_extra_types.coordinate import Latitude, Longitude

from live_calls import get_calls

from lijnpy._rest_adapter import DeLijnAPIException, RestAdapter, Result
from lijnpy.enums import Language, OperationType, TransportType
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
    assert len(colors) == 5


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
    assert len(municipalities) == 5


def test_stops_by_entity():
    stops = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/stops_by_entity.json"
        ).get_stops(1)
    )
    assert len(stops) == 5


def test_lines_by_entity():
    lines = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/lines_by_entity.json"
        ).get_lines(1)
    )
    assert len(lines) == 5


def get_client_for_line(**changes):
    """Client that returns one line from the fixture, with fields overridden.

    A value of None removes the field from the line.
    """
    with Path("tests/inputs/kods_client/v1/lines_by_entity.json").open() as file:
        line = json.load(file)["lijnen"][0]
    for key, value in changes.items():
        if value is None:
            line.pop(key, None)
        else:
            line[key] = value
    return KODSClientV1(http_client=get_async_http_mock(data={"lijnen": [line]}))


@pytest.mark.parametrize(
    "bedieningtype, expected",
    [
        ("NORMAAL", OperationType.NORMAL),
        ("SNELDIENST", OperationType.EXPRESS),
        ("SCHOOLBUS", OperationType.SCHOOL),
        ("FABRIEKSLIJN", OperationType.FACTORY),
        ("NACHTLIJN", OperationType.NIGHT),
        ("TECHNISCHE_LIJN", OperationType.TECHNICAL),
        ("BELBUS", OperationType.CALL_BUS),
        ("FLEX", OperationType.FLEX),
    ],
)
def test_line_operation_type(bedieningtype: str, expected: OperationType):
    line = asyncio.run(get_client_for_line(bedieningtype=bedieningtype).get_lines(1))[0]
    assert line.operation_type == expected


@pytest.mark.parametrize(
    "vervoertype, expected",
    [
        ("BUS", TransportType.BUS),
        ("TRAM", TransportType.TRAM),
        ("METRO", TransportType.METRO),
        ("TREIN", TransportType.TRAIN),
        ("ALLE", TransportType.ALL),
    ],
)
def test_line_transport_type(vervoertype: str, expected: TransportType):
    line = asyncio.run(get_client_for_line(vervoertype=vervoertype).get_lines(1))[0]
    assert line.transport_type == expected


def test_line_without_transport_region_code():
    line = asyncio.run(get_client_for_line(vervoerRegioCode=None).get_lines(1))[0]
    assert line.transport_region_code is None


def test_line_with_transport_region_code():
    line = asyncio.run(get_client_for_line(vervoerRegioCode="AN").get_lines(1))[0]
    assert line.transport_region_code == "AN"


def test_line_unknown_operation_type_is_rejected():
    with pytest.raises(DeLijnAPIException):
        asyncio.run(get_client_for_line(bedieningtype="HOVERCRAFT").get_lines(1))


def test_municipalities():
    municipalities = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/municipalities.json"
        ).get_municipalities()
    )
    assert len(municipalities) == 5


def test_stops():
    stops = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/stops_by_municipality.json"
        ).get_stops(1866)
    )
    assert len(stops) == 1


def test_lines():
    lines_response = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/lines_by_municipality.json"
        ).get_lines(1866)
    )
    assert len(lines_response) == 3


def test_municipality():
    municipality = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/municipality.json"
        ).get_municipality(482)
    )
    assert municipality.number == 482
    assert municipality.description == "HILVARENBEEK"
    assert municipality.main_municipality is not None
    assert municipality.main_municipality.number == 483
    assert municipality.main_municipality.description == "HILVARENBEEK"


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
    assert len(stops_in_vicinity) == 5


def test_stop():
    stop = asyncio.run(
        get_client_for_json("tests/inputs/kods_client/v1/stop.json").get_stop(
            1, 102675
        )
    )
    assert stop.entity_number == 1
    assert stop.number == 102675
    assert stop.description == "Groenplaats"
    assert stop.description_long == "Antwerpen Groenplaats"
    assert stop.municipality_number == 4390
    assert stop.municipality_description == "Antwerpen"
    assert stop.geo_coordinate.latitude == 51.2187
    assert stop.geo_coordinate.longitude == 4.40158
    assert stop.accessibilities == []
    assert stop.is_main is None
    assert stop.language == Language.DUTCH


@pytest.mark.parametrize(
    "taal, expected",
    [
        ("NEDERLANDS", Language.DUTCH),
        ("FRANS", Language.FRENCH),
        ("TWEETALIG", Language.BILINGUAL),
        ("?", Language.UNKNOWN),
    ],
)
def test_stop_language(taal: str, expected: Language):
    with Path("tests/inputs/kods_client/v1/stop.json").open() as file:
        data = json.load(file)
    data["taal"] = taal
    client = KODSClientV1(http_client=get_async_http_mock(data=data))
    stop = asyncio.run(client.get_stop(1, 102675))
    assert stop.language == expected


def test_stop_unknown_language_is_rejected():
    with Path("tests/inputs/kods_client/v1/stop.json").open() as file:
        data = json.load(file)
    data["taal"] = "KLINGON"
    client = KODSClientV1(http_client=get_async_http_mock(data=data))
    with pytest.raises(DeLijnAPIException):
        asyncio.run(client.get_stop(1, 102675))


def test_timetable():
    timetable = asyncio.run(
        get_client_for_json("tests/inputs/kods_client/v1/timetable.json").get_timetable(
            4, 408581
        )
    )
    assert len(timetable.passages) == 5
    assert len(timetable.ride_notes) == 0
    assert len(timetable.passage_notes) == 0
    assert len(timetable.detours) == 0


def test_directions():
    directions = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/directions.json"
        ).get_directions(4, 408581)
    )
    assert len(directions) == 5


def test_detours():
    detours = asyncio.run(
        get_client_for_json("tests/inputs/kods_client/v1/detours.json").get_detours(
            3, 308530
        )
    )
    assert len(detours) == 0


def test_real_time_timetable():
    real_time_timetable = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/real_time_timetable.json"
        ).get_real_time_timetable(4, 403022)
    )
    assert len(real_time_timetable.passages) == 5
    assert len(real_time_timetable.ride_notes) == 0
    assert len(real_time_timetable.passage_notes) == 0
    assert len(real_time_timetable.detours) == 0


def test_disruption():
    disruptions_response = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/disruptions.json"
        ).get_disruptions(4, 403022)
    )
    assert len(disruptions_response) == 0


def test_transport_regions():
    transport_regions = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/transport_regions.json"
        ).get_transport_regions()
    )
    assert len(transport_regions) == 5


def test_transport_region():
    vervoerregio = asyncio.run(
        get_client_for_json(
            "tests/inputs/kods_client/v1/transport_region.json"
        ).get_transport_region("AA")
    )
    assert vervoerregio.code == "AN"
    assert vervoerregio.name == "Antwerpen"
    assert vervoerregio.number == 2


def test_live_calls_cover_every_client_method():
    """Adding a client method without a live call (and fixture) fails here."""
    methods = {
        name
        for name, _ in inspect.getmembers(KODSClientV1, inspect.iscoroutinefunction)
        if name.startswith("get_")
    }
    assert methods == get_calls(KODSClientV1()).keys()
