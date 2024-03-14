from unittest import mock

from lijnpy.kods.api.v1.entities import (
    get_entities,
    get_entity,
    get_lines,
    get_municipalities,
    get_stops,
)
from tests.utils import input_as_response


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/entities/entities.json"),
)
def test_entities(_):
    entities = get_entities()
    assert len(entities) == 5


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/entities/entity.json"),
)
def test_entity(_):
    entiteit = get_entity(1)
    assert entiteit.number == 1
    assert entiteit.code == "A"
    assert entiteit.description == "Antwerpen"


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/entities/municipalities.json"
    ),
)
def test_municipalities(_):
    municipalities = get_municipalities(1)
    assert len(municipalities) == 341


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/entities/stops.json"),
)
def test_stops(_):
    stops = get_stops(1)
    assert len(stops) == 6801


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/entities/lines.json"),
)
def test_lines(_):
    lines = get_lines(1)
    assert len(lines) == 286
