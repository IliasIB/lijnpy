from unittest import mock

from lijnpy.kods.api.v1.colors import get_color, get_colors
from tests.utils import input_as_response


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/colors/colors.json"),
)
def test_colors(_):
    colors = get_colors()
    assert len(colors.colors) == 24
    assert colors.links is not None
    assert len(colors.links) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response("tests/inputs/kods/api/v1/colors/color.json"),
)
def test_color(_):
    kleur = get_color("TU")
    assert kleur.code == "TU"
    assert kleur.description == "Turkoois"
    assert kleur.rgb.red == 0
    assert kleur.rgb.green == 153
    assert kleur.rgb.blue == 170
    assert kleur.hex == "0099AA"
