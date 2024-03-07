from datetime import date
from unittest import mock

from lijnpy.kern_open_data_services_api.v1.vervoerregios import (
    get_lijnen_by_vervoerregio_code,
    get_vervoerregio_by_code,
    get_vervoerregios,
)
from tests.utils import get_good_request_input


def test_vervoerregios():
    response = get_good_request_input(
        "tests/kern_open_data_services_api/v1/inputs/vervoer_regios.json"
    )
    with mock.patch("requests.request", return_value=response):
        vervoerregios = get_vervoerregios()
        assert vervoerregios[0].code == "AA"
        assert vervoerregios[0].naam == "Aalst"
        assert vervoerregios[0].nr == 1


def test_vervoerregio_by_code():
    response = get_good_request_input(
        "tests/kern_open_data_services_api/v1/inputs/vervoer_regio.json"
    )
    with mock.patch("requests.request", return_value=response):
        vervoerregio = get_vervoerregio_by_code("AA")
        assert vervoerregio.code == "AA"
        assert vervoerregio.naam == "Aalst"
        assert vervoerregio.nr == 1


def test_get_lijnen_by_vervoerregio_code():
    response = get_good_request_input(
        "tests/kern_open_data_services_api/v1/inputs/lijnen.json"
    )
    with mock.patch("requests.request", return_value=response):
        lijnen = get_lijnen_by_vervoerregio_code("AN")
        assert lijnen[0].entiteitnummer == 1
        assert lijnen[0].lijnnummer == 63
        assert lijnen[0].lijnnummer_publiek == "Flex"
        assert lijnen[0].omschrijving == "Regio Antwerpen (Rechteroever)"
        assert lijnen[0].vervoer_regio_code == "AN"
        assert lijnen[0].publiek is True
        assert lijnen[0].vervoertype == "BUS"
        assert lijnen[0].bedieningtype == "NACHTLIJN"
        assert lijnen[0].lijn_geldig_van == date.fromisoformat("2024-02-19")
        assert lijnen[0].lijn_geldig_tot == date.fromisoformat("2099-12-01")
