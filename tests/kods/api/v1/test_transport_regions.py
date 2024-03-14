from unittest import mock

import pytest

from lijnpy.kods.api.v1.transport_regions import (
    get_lines,
    get_transport_region,
    get_transport_regions,
)
from lijnpy.rest_adapter import DeLijnAPIException
from tests.utils import input_as_response


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/transport_regions/transport_regions.json"
    ),
)
def test_transport_regions(_):
    transport_regions = get_transport_regions()
    assert len(transport_regions) == 15


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/empty.json"),
)
def test_transport_regions_empty(_):
    with pytest.raises(DeLijnAPIException):
        get_transport_regions()


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/transport_regions/transport_region.json"
    ),
)
def test_transport_region(_):
    vervoerregio = get_transport_region("AA")
    assert vervoerregio.code == "AA"
    assert vervoerregio.name == "Aalst"
    assert vervoerregio.number == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/empty.json"),
)
def test_transport_region_empty(_):
    with pytest.raises(DeLijnAPIException):
        get_transport_region("AA")


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/inputs/kods/api/v1/transport_regions/lines.json"
    ),
)
def test_lines(_):
    lines = get_lines("AN")
    assert len(lines) == 34


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/empty.json"),
)
def test_lines_empty(_):
    with pytest.raises(DeLijnAPIException):
        get_lines("AN")
