import json
from unittest import mock

import requests

from lijnpy.kern_open_data_services_api.v1.gemeenten import (
    get_gemeente_by_gemeentenummer,
    get_gemeenten,
    get_haltes_by_gemeentenummer,
    get_haltes_by_gemeentenummers,
    get_lijnen_by_gemeentenummer,
)

response = requests.Response()


def test_gemeenten_good_request():
    response.status_code = 200
    response.reason = "OK"
    gemeenten_dict = {
        "gemeenten": [
            {
                "gemeentenummer": 1,
                "omschrijving": "Test",
                "links": [
                    {
                        "rel": "self",
                        "url": "https://api.delijn.be/DLKernOpenData/api/v1/gemeenten/1",
                    }
                ],
            }
        ],
        "links": [
            {
                "rel": "self",
                "url": "https://api.delijn.be/DLKernOpenData/api/v1/gemeenten",
            }
        ],
    }
    response._content = json.dumps(gemeenten_dict).encode()
    with mock.patch("requests.request", return_value=response):
        gemeenten = get_gemeenten()
        assert gemeenten[0].gemeentenummer == 1
        assert gemeenten[0].omschrijving == "Test"
        assert gemeenten[0].links[0].rel == "self"
        assert (
            gemeenten[0].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/gemeenten/1"
        )


def test_haltes_by_gemeentenummers():
    response.status_code = 200
    response.reason = "OK"
    haltes_dict = {
        "gemeenteHaltes": [
            {
                "gemeente": {
                    "gemeentenummer": 1588,
                    "omschrijving": "ZONHOVEN",
                    "links": [
                        {
                            "rel": "detail",
                            "url": "https://api.delijn.be/DLKernOpenData/api/v1/gemeenten/1",
                        }
                    ],
                },
                "haltes": [
                    {
                        "entiteitnummer": "4",
                        "haltenummer": "403022",
                        "omschrijving": "Hulsbergweg",
                        "omschrijvingLang": "Zonhoven Hulsbergweg",
                        "gemeentenummer": 1588,
                        "omschrijvingGemeente": "Zonhoven",
                        "geoCoordinaat": {"latitude": 51.004652, "longitude": 5.346613},
                        "halteToegankelijkheden": [],
                        "hoofdHalte": None,
                        "taal": "?",
                        "links": [
                            {
                                "rel": "detail",
                                "url": "https://api.delijn.be/DLKernOpenData/api/v1/haltes/4/403022",
                            }
                        ],
                    },
                ],
            },
        ]
    }
    response._content = json.dumps(haltes_dict).encode()
    with mock.patch("requests.request", return_value=response):
        haltes = get_haltes_by_gemeentenummers([1588])
        assert haltes[0].entiteitnummer == "4"
        assert haltes[0].haltenummer == "403022"
        assert haltes[0].omschrijving == "Hulsbergweg"
        assert haltes[0].omschrijving_lang == "Zonhoven Hulsbergweg"
        assert haltes[0].gemeentenummer == 1588
        assert haltes[0].omschrijving_gemeente == "Zonhoven"
        assert haltes[0].geo_coordinaat.latitude == 51.004652
        assert haltes[0].geo_coordinaat.longitude == 5.346613
        assert haltes[0].halte_toegankelijkheden == []
        assert haltes[0].hoofd_halte is None
        assert haltes[0].taal == "?"
        assert haltes[0].links[0].rel == "detail"
        assert (
            haltes[0].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/haltes/4/403022"
        )


def test_haltes_by_gemeentenummer():
    response.status_code = 200
    response.reason = "OK"
    haltes_dict = {
        # TODO: Move this to a separate file
        "haltes": [
            {
                "entiteitnummer": "4",
                "haltenummer": "403022",
                "omschrijving": "Hulsbergweg",
                "omschrijvingLang": "Zonhoven Hulsbergweg",
                "gemeentenummer": 1588,
                "omschrijvingGemeente": "Zonhoven",
                "geoCoordinaat": {"latitude": 51.004652, "longitude": 5.346613},
                "halteToegankelijkheden": [],
                "hoofdHalte": None,
                "taal": "?",
                "links": [
                    {
                        "rel": "detail",
                        "url": "https://api.delijn.be/DLKernOpenData/api/v1/haltes/4/403022",
                    }
                ],
            },
        ]
    }
    response._content = json.dumps(haltes_dict).encode()
    with mock.patch("requests.request", return_value=response):
        haltes = get_haltes_by_gemeentenummer(1588)
        assert haltes[0].entiteitnummer == "4"
        assert haltes[0].haltenummer == "403022"
        assert haltes[0].omschrijving == "Hulsbergweg"
        assert haltes[0].omschrijving_lang == "Zonhoven Hulsbergweg"
        assert haltes[0].gemeentenummer == 1588
        assert haltes[0].omschrijving_gemeente == "Zonhoven"
        assert haltes[0].geo_coordinaat.latitude == 51.004652
        assert haltes[0].geo_coordinaat.longitude == 5.346613
        assert haltes[0].halte_toegankelijkheden == []
        assert haltes[0].hoofd_halte is None
        assert haltes[0].taal == "?"
        assert haltes[0].links[0].rel == "detail"
        assert (
            haltes[0].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/haltes/4/403022"
        )


def test_lijnen_by_gemeentenummer():
    response.status_code = 200
    response.reason = "OK"
    lijnen_dict = {
        "lijnen": [
            {
                "entiteitnummer": "4",
                "lijnnummer": "196",
                "lijnnummerPubliek": "196",
                "omschrijving": "Bocholt - Hasselt",
                "vervoerRegioCode": "LI",
                "publiek": True,
                "vervoertype": "BUS",
                "bedieningtype": "NORMAAL",
                "lijnGeldigVan": "2024-03-04",
                "lijnGeldigTot": "2024-03-31",
                "links": [
                    {
                        "rel": "detail",
                        "url": "https://api.delijn.be/DLKernOpenData/api/v1/lijnen/4/196",
                    }
                ],
            }
        ]
    }
    response._content = json.dumps(lijnen_dict).encode()
    with mock.patch("requests.request", return_value=response):
        lijnen = get_lijnen_by_gemeentenummer(1588)
        assert lijnen[0].entiteitnummer == "4"
        assert lijnen[0].lijnnummer == "196"
        assert lijnen[0].lijnnummer_publiek == "196"
        assert lijnen[0].omschrijving == "Bocholt - Hasselt"
        assert lijnen[0].vervoer_regio_code == "LI"
        assert lijnen[0].publiek is True
        assert lijnen[0].vervoertype == "BUS"
        assert lijnen[0].bedieningtype == "NORMAAL"
        assert lijnen[0].lijn_geldig_van == "2024-03-04"
        assert lijnen[0].lijn_geldig_tot == "2024-03-31"
        assert lijnen[0].links[0].rel == "detail"
        assert (
            lijnen[0].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/lijnen/4/196"
        )


def test_gemeente_by_gemeentenummer():
    response.status_code = 200
    response.reason = "OK"
    gemeente_dict = {
        "gemeentenummer": 1588,
        "omschrijving": "ZONHOVEN",
        "links": [
            {
                "rel": "self",
                "url": "https://api.delijn.be/DLKernOpenData/api/v1/gemeenten/1",
            }
        ],
    }
    response._content = json.dumps(gemeente_dict).encode()
    with mock.patch("requests.request", return_value=response):
        gemeente = get_gemeente_by_gemeentenummer(1)
        assert gemeente.gemeentenummer == 1588
        assert gemeente.omschrijving == "ZONHOVEN"
        assert gemeente.links[0].rel == "self"
        assert (
            gemeente.links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/gemeenten/1"
        )
