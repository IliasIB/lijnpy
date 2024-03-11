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
    assert len(entities.entities) == 5
    assert isinstance(entities.links, list)
    assert len(entities.links) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/entities/entity.json"),
)
def test_entity(_):
    entiteit = get_entity(1)
    assert entiteit.number == 1
    assert entiteit.code == "A"
    assert entiteit.description == "Antwerpen"
    assert isinstance(entiteit.links, list)
    assert len(entiteit.links) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/entities/municipalities.json"
    ),
)
def test_municipalities(_):
    municipalities = get_municipalities(1)
    assert len(municipalities.municipalities) == 341
    assert municipalities.links is not None
    assert len(municipalities.links) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/entities/stops.json"),
)
def test_stops(_):
    stops = get_stops(1)
    assert len(stops.stops) == 6801
    assert isinstance(stops.links, list)
    assert len(stops.links) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/entities/lines.json"),
)
def test_lines(_):
    lines = get_lines(1)
    assert len(lines.lines) == 286
    assert lines.links is not None
    assert len(lines.links) == 1
