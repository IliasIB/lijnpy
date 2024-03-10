from unittest import mock

from lijnpy.kods.api.v1.municipalities import (
    get_lines,
    get_municipalities,
    get_municipality,
    get_stops,
)
from tests.utils import input_as_response


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/municipalities/municipalities.json"
    ),
)
def test_municipalities(_):
    municipalities = get_municipalities()
    assert len(municipalities.municipalities) == 1913
    assert municipalities.links is not None
    assert len(municipalities.links) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/municipalities/stops.json"
    ),
)
def test_stops(_):
    stops_response = get_stops(1866)
    assert len(stops_response.stops) == 417
    assert stops_response.links is not None
    assert len(stops_response.links) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/municipalities/lines.json"
    ),
)
def test_lines(_):
    lines_response = get_lines(1866)
    assert len(lines_response.lines) == 74
    assert lines_response.links is not None
    assert len(lines_response.links) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/municipalities/municipality.json"
    ),
)
def test_municipality(_):
    gemeente = get_municipality(1)
    assert gemeente.number == 1491
    assert gemeente.description == "HOUTHALEN"
    assert gemeente.main_municipality is not None
    assert gemeente.main_municipality.number == 1422
    assert gemeente.main_municipality.description == "HOUTHALEN-HELCHTEREN"
    assert gemeente.links is not None
    assert len(gemeente.links) == 1
