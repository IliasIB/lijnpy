from unittest import mock

from lijnpy.kern_open_data_services_api.v1.entities import (
    get_entities,
    get_entity,
    get_lines,
    get_municipality,
    get_stops,
)
from tests.utils import input_as_response


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/entiteiten.json"
    ),
)
def test_entities(_):
    entiteiten = get_entities()
    assert entiteiten[0].number == 1
    assert entiteiten[0].code == "L"
    assert entiteiten[0].description == "Limburg"


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/entiteit.json"
    ),
)
def test_entity(_):
    entiteit = get_entity(1)
    assert entiteit.number == 1
    assert entiteit.code == "A"
    assert entiteit.description == "Antwerpen"


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/gemeenten.json"
    ),
)
def test_municipalities(_):
    gemeenten = get_municipality(1)
    assert len(gemeenten) == 2


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/haltes.json"
    ),
)
def test_stops(_):
    haltes = get_stops(1)
    assert len(haltes) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/lijnen.json"
    ),
)
def test_lines(_):
    lijnen = get_lines(1)
    assert len(lijnen) == 1
