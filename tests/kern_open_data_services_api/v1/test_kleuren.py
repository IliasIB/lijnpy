import json
from unittest import mock

import requests

from lijnpy.kern_open_data_services_api.v1.kleuren import get_kleur_by_code, get_kleuren

response = requests.Response()


def test_kleuren():
    response.status_code = 200
    response.reason = "OK"
    entiteiten_dict = {
        "kleuren": [
            {
                "code": "TU",
                "omschrijving": "Turkoois",
                "rgb": {"rood": 0, "groen": 153, "blauw": 170},
                "hex": "0099AA",
                "links": [
                    {
                        "rel": "detail",
                        "url": "https://api.delijn.be/DLKernOpenData/api/v1/kleuren/TU",
                    }
                ],
            }
        ]
    }
    response._content = json.dumps(entiteiten_dict).encode()
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
    response.status_code = 200
    response.reason = "OK"
    kleur_dict = {
        "code": "BD",
        "omschrijving": "Blauw De Lijn",
        "rgb": {"rood": 0, "groen": 0, "blauw": 153},
        "hex": "000099",
        "links": [
            {
                "rel": "self",
                "url": "https://api.delijn.be/DLKernOpenData/api/v1/kleuren/BD",
            }
        ],
    }
    response._content = json.dumps(kleur_dict).encode()
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
