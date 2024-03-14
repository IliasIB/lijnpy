from unittest import mock

import pytest

from lijnpy._rest_adapter import DeLijnAPIException
from lijnpy.kods.api.v1.colors import get_color, get_colors
from tests.utils import input_as_response


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/colors/colors.json"),
)
def test_colors(_):
    colors = get_colors()
    assert len(colors) == 24


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/empty.json"),
)
def test_colors_empty(_):
    with pytest.raises(DeLijnAPIException):
        get_colors()


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/colors/color.json"),
)
def test_color(_):
    color = get_color("TU")
    assert color.code == "TU"
    assert color.description == "Turkoois"
    assert color.color.as_hex() == "#09a"


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/empty.json"),
)
def test_color_empty(_):
    with pytest.raises(DeLijnAPIException):
        get_color("TU")
