from unittest import mock

from lijnpy.kern_open_data_services_api.v1.colors import get_color, get_colors
from tests.utils import input_as_response


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/kleuren.json"
    ),
)
def test_colors(_):
    kleuren = get_colors()
    assert len(kleuren) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/kleur.json"
    ),
)
def test_color(_):
    kleur = get_color("TU")
    assert kleur.code == "BD"
    assert kleur.description == "Blauw De Lijn"
    assert kleur.rgb.red == 0
    assert kleur.rgb.green == 0
    assert kleur.rgb.blue == 153
    assert kleur.hex == "000099"
