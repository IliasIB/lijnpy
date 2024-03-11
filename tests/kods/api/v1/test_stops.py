from unittest import mock

from lijnpy.kods.api.v1.models.utils import GeoCoordinate
from lijnpy.kods.api.v1.stops import (
    get_detours,
    get_directions,
    get_disruptions,
    get_real_time_passages,
    get_stop,
    get_stops_in_vicinity,
    get_timetable,
)
from tests.utils import input_as_response


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/stops/stops_in_vicinity.json"
    ),
)
def test_stops_in_vicinity(_):
    stops_in_vicinity_response = get_stops_in_vicinity(
        GeoCoordinate(latitude=51.004652, longitude=5.346613)
    )
    assert len(stops_in_vicinity_response.stops) == 7
    assert stops_in_vicinity_response.links is not None
    assert len(stops_in_vicinity_response.links) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/stops/stop.json"),
)
def test_stop(_):
    stop_response = get_stop(4, 408581)
    assert stop_response.entity_number == 4
    assert stop_response.number == 408581
    assert stop_response.description == "Koning Boudewijnlaan"
    assert stop_response.description_long == "Heverlee Koning Boudewijnlaan"
    assert stop_response.municipality_number == 1866
    assert stop_response.omschrijving_gemeente == "Leuven"
    assert stop_response.geo_coordinate.latitude == 50.868276
    assert stop_response.geo_coordinate.longitude == 4.68115
    assert stop_response.accessibilities == [
        "MOTORISCH_MET_ASSIST",
        "MOTORISCHE_BEPERKING",
    ]
    assert stop_response.is_main is None
    assert stop_response.language == "?"
    assert stop_response.links is not None
    assert len(stop_response.links) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/stops/timetable.json"),
)
def test_timetable(_):
    timetable_response = get_timetable(4, 408581)
    assert len(timetable_response.passages) == 1
    assert timetable_response.links is not None
    assert len(timetable_response.links) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/stops/directions.json"),
)
def test_directions(_):
    directions_response = get_directions(4, 408581)
    assert len(directions_response.directions) == 2
    assert directions_response.links is not None
    assert len(directions_response.links) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/stops/detours.json"),
)
def test_detours(_):
    detours_response = get_detours(3, 308530)
    assert len(detours_response.detours) == 1
    assert detours_response.links is not None
    assert len(detours_response.links) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/stops/real_time_passages.json"
    ),
)
def test_real_time_passages(_):
    real_time_passages_response = get_real_time_passages(4, 403022)
    assert len(real_time_passages_response.passages) == 1
    assert real_time_passages_response.links is not None
    assert len(real_time_passages_response.links) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/stops/disruptions.json"),
)
def test_disruption(_):
    disruptions_response = get_disruptions(4, 403022)
    assert len(disruptions_response.disruptions) == 1
    assert disruptions_response.links is not None
    assert len(disruptions_response.links) == 1
