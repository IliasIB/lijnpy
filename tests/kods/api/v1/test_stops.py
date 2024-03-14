from typing import cast
from unittest import mock

import pytest
from pydantic_extra_types.coordinate import Latitude, Longitude

from lijnpy.kods.api.v1.enums import Accessibility, Language
from lijnpy.kods.api.v1.models import GeoCoordinate
from lijnpy.kods.api.v1.stops import (
    get_detours,
    get_directions,
    get_disruptions,
    get_real_time_timetable,
    get_stop,
    get_stops_in_vicinity,
    get_timetable,
)
from lijnpy.rest_adapter import DeLijnAPIException
from tests.utils import input_as_response


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/stops/stops_in_vicinity.json"
    ),
)
def test_stops_in_vicinity(_):
    stops_in_vicinity = get_stops_in_vicinity(
        GeoCoordinate(
            latitude=cast(Latitude, 51.004652), longitude=cast(Longitude, 5.346613)
        )
    )
    assert len(stops_in_vicinity) == 7


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/empty.json"),
)
def test_stops_in_vicinity_empty(_):
    with pytest.raises(DeLijnAPIException):
        get_stops_in_vicinity(
            GeoCoordinate(
                latitude=cast(Latitude, 51.004652), longitude=cast(Longitude, 5.346613)
            )
        )


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/stops/stop.json"),
)
def test_stop(_):
    stop = get_stop(4, 408581)
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


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/empty.json"),
)
def test_stop_empty(_):
    with pytest.raises(DeLijnAPIException):
        get_stop(4, 408581)


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/stops/timetable.json"),
)
def test_timetable(_):
    timetable = get_timetable(4, 408581)
    assert len(timetable.passages) == 2
    assert len(timetable.ride_notes) == 0
    assert len(timetable.passage_notes) == 0
    assert len(timetable.detours) == 0


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/empty.json"),
)
def test_timetable_empty(_):
    with pytest.raises(DeLijnAPIException):
        get_timetable(4, 408581)


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/stops/directions.json"),
)
def test_directions(_):
    directions = get_directions(4, 408581)
    assert len(directions) == 2


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/empty.json"),
)
def test_directions_empty(_):
    with pytest.raises(DeLijnAPIException):
        get_directions(4, 408581)


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/stops/detours.json"),
)
def test_detours(_):
    detours = get_detours(3, 308530)
    assert len(detours) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/empty.json"),
)
def test_detours_empty(_):
    with pytest.raises(DeLijnAPIException):
        get_detours(3, 308530)


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/stops/real_time_timetable.json"
    ),
)
def test_real_time_timetable(_):
    real_time_timetable = get_real_time_timetable(4, 403022)
    assert len(real_time_timetable.passages) == 1
    assert len(real_time_timetable.ride_notes) == 0
    assert len(real_time_timetable.passage_notes) == 0
    assert len(real_time_timetable.detours) == 0


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/empty.json"),
)
def test_real_time_timetable_empty(_):
    with pytest.raises(DeLijnAPIException):
        get_real_time_timetable(4, 403022)


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/stops/disruptions.json"),
)
def test_disruption(_):
    disruptions_response = get_disruptions(4, 403022)
    assert len(disruptions_response) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/empty.json"),
)
def test_disruption_empty(_):
    with pytest.raises(DeLijnAPIException):
        get_disruptions(4, 403022)
