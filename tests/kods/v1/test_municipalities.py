from unittest import mock

from lijnpy.kods.v1.municipalities import (
    get_lines,
    get_municipalities,
    get_municipality,
    get_stops,
)
from tests.utils import input_as_response


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/kods/v1/inputs/gemeenten.json"),
)
def test_municipalities(_):
    gemeenten = get_municipalities()
    assert len(gemeenten) == 2


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/kods/v1/inputs/haltes.json"),
)
def test_stops(_):
    haltes = get_stops(1350)
    assert len(haltes) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/kods/v1/inputs/lijnen.json"),
)
def test_lines(_):
    lijnen = get_lines(1588)
    assert len(lijnen) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/kods/v1/inputs/gemeente.json"),
)
def test_municipality(_):
    gemeente = get_municipality(1)
    assert gemeente.number == 951
    assert gemeente.description == "KALMTHOUT"
    assert gemeente.main_municipality is not None
    assert gemeente.main_municipality.number == 937
    assert gemeente.main_municipality.description == "KALMTHOUT"
