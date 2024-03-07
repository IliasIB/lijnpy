from unittest import mock

from lijnpy.kern_open_data_services_api.v1.kleuren import get_kleur_by_code, get_kleuren
from tests.utils import get_good_request_input


def test_kleuren():
    response = get_good_request_input(
        "tests/kern_open_data_services_api/v1/inputs/kleuren.json"
    )
    with mock.patch("requests.request", return_value=response):
        kleuren = get_kleuren()
        assert kleuren[0].code == "TU"
        assert kleuren[0].omschrijving == "Turkoois"
        assert kleuren[0].rgb.rood == 0
        assert kleuren[0].rgb.groen == 153
        assert kleuren[0].rgb.blauw == 170
        assert kleuren[0].hex == "0099AA"
        assert kleuren[0].links[0].rel == "detail"
        assert (
            kleuren[0].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/kleuren/TU"
        )


def test_kleur_by_code():
    response = get_good_request_input(
        "tests/kern_open_data_services_api/v1/inputs/kleur.json"
    )
    with mock.patch("requests.request", return_value=response):
        kleur = get_kleur_by_code("TU")
        assert kleur.code == "BD"
        assert kleur.omschrijving == "Blauw De Lijn"
        assert kleur.rgb.rood == 0
        assert kleur.rgb.groen == 0
        assert kleur.rgb.blauw == 153
        assert kleur.hex == "000099"
        assert kleur.links[0].rel == "self"
        assert (
            kleur.links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/kleuren/BD"
        )
