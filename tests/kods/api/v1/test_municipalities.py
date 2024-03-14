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
    assert len(municipalities) == 1913


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/municipalities/stops.json"
    ),
)
def test_stops(_):
    stops = get_stops(1866)
    assert len(stops) == 417


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/municipalities/lines.json"
    ),
)
def test_lines(_):
    lines_response = get_lines(1866)
    assert len(lines_response) == 74


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
