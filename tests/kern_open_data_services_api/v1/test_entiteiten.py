import json
from unittest import mock

import requests

from lijnpy.kern_open_data_services_api.v1.entiteiten import (
    get_entiteit_by_entiteitnummer,
    get_entiteiten,
    get_gemeenten_by_entiteitsnummer,
    get_haltes_by_entiteitsnummer,
    get_lijnen_by_entiteitsnummer,
)

response = requests.Response()


def test_entiteiten():
    response.status_code = 200
    response.reason = "OK"
    entiteiten_dict = {
        "entiteiten": [
            {
                "entiteitnummer": "1",
                "entiteitcode": "A",
                "omschrijving": "Antwerpen",
                "links": [{"rel": "string", "url": "string"}],
            }
        ]
    }
    response._content = json.dumps(entiteiten_dict).encode()
    with mock.patch("requests.request", return_value=response):
        entiteiten = get_entiteiten()
        assert entiteiten[0].entiteitnummer == "1"
        assert entiteiten[0].entiteitcode == "A"
        assert entiteiten[0].omschrijving == "Antwerpen"
        assert entiteiten[0].links[0].rel == "string"
        assert entiteiten[0].links[0].url == "string"


def test_entiteit_by_entiteitnummer():
    response.status_code = 200
    response.reason = "OK"
    entiteit_dict = {
        "entiteitnummer": "1",
        "entiteitcode": "A",
        "omschrijving": "Antwerpen",
        "links": [{"rel": "string", "url": "string"}],
    }
    response._content = json.dumps(entiteit_dict).encode()
    with mock.patch("requests.request", return_value=response):
        entiteit = get_entiteit_by_entiteitnummer("1")
        assert entiteit.entiteitnummer == "1"
        assert entiteit.entiteitcode == "A"
        assert entiteit.omschrijving == "Antwerpen"
        assert entiteit.links[0].rel == "string"
        assert entiteit.links[0].url == "string"


def test_gemeenten_by_entiteitsnummer():
    response.status_code = 200
    response.reason = "OK"
    gemeenten_dict = {
        "gemeenten": [
            {
                "gemeentenummer": 922,
                "omschrijving": "HOOGSTRATEN",
                "links": [{"rel": "string", "url": "string"}],
            }
        ]
    }
    response._content = json.dumps(gemeenten_dict).encode()
    with mock.patch("requests.request", return_value=response):
        gemeenten = get_gemeenten_by_entiteitsnummer("1")
        assert gemeenten[0].gemeentenummer == 922
        assert gemeenten[0].omschrijving == "HOOGSTRATEN"
        assert gemeenten[0].links[0].rel == "string"
        assert gemeenten[0].links[0].url == "string"


def test_haltes_by_entiteitsnummer():
    response.status_code = 200
    response.reason = "OK"
    haltes_dict = {
        "haltes": [
            {
                "entiteitnummer": "1",
                "haltenummer": "100118",
                "omschrijving": "Station",
                "omschrijvingLang": "Bornem Station",
                "gemeentenummer": 1350,
                "omschrijvingGemeente": "Bornem",
                "geoCoordinaat": {"latitude": 51.099532, "longitude": 4.240739},
                "halteToegankelijkheden": [],
                "hoofdHalte": None,
                "taal": "?",
                "links": [
                    {
                        "rel": "detail",
                        "url": "https://api.delijn.be/DLKernOpenData/api/v1/haltes/1/100118",
                    }
                ],
            }
        ]
    }
    response._content = json.dumps(haltes_dict).encode()
    with mock.patch("requests.request", return_value=response):
        haltes = get_haltes_by_entiteitsnummer("1")
        assert haltes[0].entiteitnummer == "1"
        assert haltes[0].haltenummer == "100118"
        assert haltes[0].omschrijving == "Station"
        assert haltes[0].omschrijving_lang == "Bornem Station"
        assert haltes[0].gemeentenummer == 1350
        assert haltes[0].omschrijving_gemeente == "Bornem"
        assert haltes[0].geo_coordinaat.latitude == 51.099532
        assert haltes[0].geo_coordinaat.longitude == 4.240739
        assert haltes[0].halte_toegankelijkheden == []
        assert haltes[0].hoofd_halte is None
        assert haltes[0].taal == "?"
        assert haltes[0].links[0].rel == "detail"
        assert (
            haltes[0].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/haltes/1/100118"
        )


def test_lijnen_by_entiteitsnummer():
    response.status_code = 200
    response.reason = "OK"
    lijnen_dict = {
        "lijnen": [
            {
                "entiteitnummer": "1",
                "lijnnummer": "63",
                "lijnnummerPubliek": "Flex",
                "omschrijving": "Regio Antwerpen (Rechteroever)",
                "vervoerRegioCode": "AN",
                "publiek": True,
                "vervoertype": "BUS",
                "bedieningtype": "NACHTLIJN",
                "lijnGeldigVan": "2024-02-19",
                "lijnGeldigTot": "2099-12-01",
                "links": [
                    {
                        "rel": "detail",
                        "url": "https://api.delijn.be/DLKernOpenData/api/v1/lijnen/1/63",
                    }
                ],
            }
        ]
    }
    response._content = json.dumps(lijnen_dict).encode()
    with mock.patch("requests.request", return_value=response):
        lijnen = get_lijnen_by_entiteitsnummer("1")
        assert lijnen[0].entiteitnummer == "1"
        assert lijnen[0].lijnnummer == "63"
        assert lijnen[0].lijnnummer_publiek == "Flex"
        assert lijnen[0].omschrijving == "Regio Antwerpen (Rechteroever)"
        assert lijnen[0].vervoer_regio_code == "AN"
        assert lijnen[0].publiek is True
        assert lijnen[0].vervoertype == "BUS"
        assert lijnen[0].bedieningtype == "NACHTLIJN"
        assert lijnen[0].lijn_geldig_van == "2024-02-19"
        assert lijnen[0].lijn_geldig_tot == "2099-12-01"
        assert lijnen[0].links[0].rel == "detail"
        assert (
            lijnen[0].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/lijnen/1/63"
        )
