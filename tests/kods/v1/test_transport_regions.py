from unittest import mock

from lijnpy.kods.v1.transport_regions import (
    get_lines,
    get_transport_region,
    get_transport_regions,
)
from tests.utils import input_as_response


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/vervoer_regios.json"
    ),
)
def test_transport_regions(_):
    vervoerregios = get_transport_regions()
    assert len(vervoerregios) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/vervoer_regio.json"
    ),
)
def test_transport_region(_):
    vervoerregio = get_transport_region("AA")
    assert vervoerregio.code == "AA"
    assert vervoerregio.name == "Aalst"
    assert vervoerregio.number == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/lijnen.json"
    ),
)
def test_lines(_):
    lijnen = get_lines("AN")
    assert len(lijnen) == 1
