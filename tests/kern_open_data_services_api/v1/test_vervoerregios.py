import json
from unittest import mock

import requests

response = requests.Response()


def test_vervoerregios():
    response.status_code = 200
    response.reason = "OK"
    vervoerregios_dict = {
        "vervoerRegios": [
            {
                "code": "AA",
                "naam": "Aalst",
                "nr": "01",
                "links": [
                    {
                        "rel": "lijnen",
                        "url": "https://api.delijn.be/DLKernOpenData/api/v1/vervoerregios/AA/lijnen",
                    }
                ],
            }
        ]
    }
    response._content = json.dumps(vervoerregios_dict).encode()
    with mock.patch("requests.request", return_value=response):
        from lijnpy.kern_open_data_services_api.v1.vervoerregios import (
            get_vervoerregios,
        )

        vervoerregios = get_vervoerregios()
        assert vervoerregios[0].code == "AA"
        assert vervoerregios[0].naam == "Aalst"
        assert vervoerregios[0].nr == "01"
        assert vervoerregios[0].links[0].rel == "lijnen"
        assert (
            vervoerregios[0].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/vervoerregios/AA/lijnen"
        )


def test_vervoerregio_by_code():
    response.status_code = 200
    response.reason = "OK"
    vervoerregio_dict = {
        "code": "AA",
        "naam": "Aalst",
        "nr": "01",
        "links": [
            {
                "rel": "self",
                "url": "https://api.delijn.be/DLKernOpenData/api/v1/vervoerregios/AA",
            },
            {
                "rel": "lijnen",
                "url": "https://api.delijn.be/DLKernOpenData/api/v1/vervoerregios/AA/lijnen",
            },
        ],
    }
    response._content = json.dumps(vervoerregio_dict).encode()
    with mock.patch("requests.request", return_value=response):
        from lijnpy.kern_open_data_services_api.v1.vervoerregios import (
            get_vervoerregio_by_code,
        )

        vervoerregio = get_vervoerregio_by_code("AA")
        assert vervoerregio.code == "AA"
        assert vervoerregio.naam == "Aalst"
        assert vervoerregio.nr == "01"
        assert vervoerregio.links[0].rel == "self"
        assert (
            vervoerregio.links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/vervoerregios/AA"
        )


def test_get_lijnen_by_vervoerregio_code():
    response.status_code = 200
    response.reason = "OK"
    lijnen_dict = {
        "lijnen": [
            {
                "entiteitnummer": "2",
                "lijnnummer": "804",
                "lijnnummerPubliek": "804",
                "omschrijving": "Aalst - Mere - Burst - Heldergem",
                "vervoerRegioCode": "AA",
                "publiek": True,
                "vervoertype": "BUS",
                "bedieningtype": "NORMAAL",
                "lijnGeldigVan": "2024-02-26",
                "lijnGeldigTot": "2024-03-29",
                "links": [
                    {
                        "rel": "detail",
                        "url": "https://api.delijn.be/DLKernOpenData/api/v1/lijnen/2/804",
                    }
                ],
            }
        ]
    }
    response._content = json.dumps(lijnen_dict).encode()
    with mock.patch("requests.request", return_value=response):
        from lijnpy.kern_open_data_services_api.v1.vervoerregios import (
            get_lijnen_by_vervoerregio_code,
        )

        lijnen = get_lijnen_by_vervoerregio_code("AA")
        assert lijnen[0].entiteitnummer == "2"
        assert lijnen[0].lijnnummer == "804"
        assert lijnen[0].lijnnummer_publiek == "804"
        assert lijnen[0].omschrijving == "Aalst - Mere - Burst - Heldergem"
        assert lijnen[0].vervoer_regio_code == "AA"
        assert lijnen[0].publiek is True
        assert lijnen[0].vervoertype == "BUS"
        assert lijnen[0].bedieningtype == "NORMAAL"
        assert lijnen[0].lijn_geldig_van == "2024-02-26"
        assert lijnen[0].lijn_geldig_tot == "2024-03-29"
        assert lijnen[0].links[0].rel == "detail"
        assert (
            lijnen[0].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/lijnen/2/804"
        )
