import json
from pathlib import Path
from unittest import mock

import requests

from lijnpy.kern_open_data_services_api.v1.haltes import (
    get_dienstregelingen,
    get_halte,
    get_haltes,
    get_haltes_in_neighbourhood,
    get_omleidingen,
    get_real_time_doorkomsten,
    get_richtingen,
    get_storingen,
)
from lijnpy.models import GeoCoordinaat

response = requests.Response()


def test_haltes():
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
        haltes = get_haltes()
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


def test_haltes_in_neighbourhood():
    response.status_code = 200
    response.reason = "OK"
    haltes_dict = {
        "haltes": [
            {
                "type": "DELIJN",
                "id": "403022",
                "naam": "Zonhoven Hulsbergweg",
                "afstand": 0,
                "geoCoordinaat": {"latitude": 51.004652, "longitude": 5.346613},
                "links": [
                    {
                        "rel": "lijnrichtingen",
                        "url": "https://api.delijn.be/DLKernOpenData/api/v1/haltes/4/403022/lijnrichtingen",
                    },
                ],
            }
        ]
    }
    response._content = json.dumps(haltes_dict).encode()
    with mock.patch("requests.request", return_value=response):
        haltes = get_haltes_in_neighbourhood(
            GeoCoordinaat(latitude=51.004652, longitude=5.346613)
        )
        assert haltes[0].type == "DELIJN"
        assert haltes[0].id == "403022"
        assert haltes[0].naam == "Zonhoven Hulsbergweg"
        assert haltes[0].afstand == 0
        assert haltes[0].geo_coordinaat.latitude == 51.004652
        assert haltes[0].geo_coordinaat.longitude == 5.346613
        assert haltes[0].links[0].rel == "lijnrichtingen"
        assert (
            haltes[0].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/haltes/4/403022/lijnrichtingen"
        )


def test_halte():
    response.status_code = 200
    response.reason = "OK"
    halte_dict = {
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
    }
    response._content = json.dumps(halte_dict).encode()
    with mock.patch("requests.request", return_value=response):
        halte = get_halte("4", "403022")
        assert halte.entiteitnummer == "4"
        assert halte.haltenummer == "403022"
        assert halte.omschrijving == "Hulsbergweg"
        assert halte.omschrijving_lang == "Zonhoven Hulsbergweg"
        assert halte.gemeentenummer == 1588
        assert halte.omschrijving_gemeente == "Zonhoven"
        assert halte.geo_coordinaat.latitude == 51.004652
        assert halte.geo_coordinaat.longitude == 5.346613
        assert halte.halte_toegankelijkheden == []
        assert halte.hoofd_halte is None
        assert halte.taal == "?"
        assert halte.links[0].rel == "detail"
        assert (
            halte.links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/haltes/4/403022"
        )


def test_dienstregelingen():
    response.status_code = 200
    response.reason = "OK"
    dienstregeling_path = Path(
        "tests/kern_open_data_services_api/v1/inputs/dienstregeling.json"
    )
    with dienstregeling_path.open() as dienstregeling_file:
        dienstregeling = dienstregeling_file.read()
    response._content = dienstregeling.encode()
    with mock.patch("requests.request", return_value=response):
        dienstregeling = get_dienstregelingen("4", "403022")
        assert dienstregeling.doorkomsten[0].entiteitnummer == "4"
        assert dienstregeling.doorkomsten[0].lijnnummer == 465
        assert dienstregeling.doorkomsten[0].richting == "TERUG"
        assert dienstregeling.doorkomsten[0].ritnummer == 2
        assert dienstregeling.doorkomsten[0].bestemming == "Houthalen"
        assert dienstregeling.doorkomsten[0].plaats_bestemming == "Houthalen Station"
        assert dienstregeling.doorkomsten[0].vias == []
        assert (
            dienstregeling.doorkomsten[0].dienstregeling_tijdstip
            == "2024-03-07T07:38:00"
        )


def test_richtingen():
    response.status_code = 200
    response.reason = "OK"
    richtingen_path = Path(
        "tests/kern_open_data_services_api/v1/inputs/richtingen.json"
    )
    with richtingen_path.open() as richtingen_file:
        richtingen = richtingen_file.read()
    response._content = richtingen.encode()
    with mock.patch("requests.request", return_value=response):
        richtingen = get_richtingen(4, 403022)
        assert richtingen[0].entiteitnummer == "4"
        assert richtingen[0].lijnnummer == "465"
        assert richtingen[0].richting == "TERUG"
        assert richtingen[0].omschrijving == "Genk - Houthalen"
        assert richtingen[0].links[0].rel == "detail"
        assert (
            richtingen[0].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/lijnen/4/465/lijnrichtingen/TERUG"
        )
        assert richtingen[1].entiteitnummer == "4"
        assert richtingen[1].lijnnummer == "950"
        assert richtingen[1].richting == "HEEN"
        assert richtingen[1].omschrijving == "Regio Limburg"
        assert richtingen[1].links[0].rel == "detail"
        assert (
            richtingen[1].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/lijnen/4/950/lijnrichtingen/HEEN"
        )


def test_omleidingen():
    response.status_code = 200
    response.reason = "OK"
    omleidingen_path = Path(
        "tests/kern_open_data_services_api/v1/inputs/omleidingen.json"
    )
    with omleidingen_path.open() as omleidingen_file:
        omleidingen = omleidingen_file.read()
    response._content = omleidingen.encode()
    with mock.patch("requests.request", return_value=response):
        omleidingen = get_omleidingen(4, 403022)
        assert omleidingen[0].titel == "Werken thv de halte Aristide Briand"
        assert (
            omleidingen[0].omschrijving
            == "\nPeriode \nVan vrijdag 21 april 2023 tot het einde van de  werken. \n\nNiet-bediende halte \n. Anderlecht : Aristide Briand\n\n\nVervanghalte \n. Anderlecht : Aristide Briand (tijdelijk)\n\n\n"
        )
        assert omleidingen[0].periode.start_datum == "2023-04-21T00:00:00"
        assert omleidingen[0].referentie_omleiding == 873876
        assert omleidingen[0].type == "WERKEN"
        assert omleidingen[0].omleidings_dagen == [
            "MAANDAG",
            "DINSDAG",
            "WOENSDAG",
            "DONDERDAG",
            "VRIJDAG",
            "ZATERDAG",
            "ZONDAG",
        ]
        assert omleidingen[0].links[0].rel == "omleidingen"
        assert (
            omleidingen[0].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/omleidingen/873876"
        )


def test_real_time_doorkomsten():
    response.status_code = 200
    response.reason = "OK"
    real_time_doorkomsten_path = Path(
        "tests/kern_open_data_services_api/v1/inputs/realtime.json"
    )
    with real_time_doorkomsten_path.open() as real_time_doorkomsten_file:
        real_time_doorkomsten = real_time_doorkomsten_file.read()
    response._content = real_time_doorkomsten.encode()
    with mock.patch("requests.request", return_value=response):
        real_time_doorkomsten = get_real_time_doorkomsten(4, 403022)
        assert real_time_doorkomsten[0].entiteitnummer == "4"
        assert real_time_doorkomsten[0].lijnnummer == 465
        assert real_time_doorkomsten[0].richting == "TERUG"
        assert real_time_doorkomsten[0].ritnummer == "16"
        assert real_time_doorkomsten[0].bestemming == "Houthalen"
        assert real_time_doorkomsten[0].vias == []
        assert real_time_doorkomsten[0].dienstregeling_tijdstip == "2024-03-07T17:05:00"
        assert real_time_doorkomsten[0].real_time_tijdstip == "2024-03-07T17:05:20"
        assert real_time_doorkomsten[0].vrtnum == "442079"
        assert real_time_doorkomsten[0].prediction_statussen == ["REALTIME"]
        assert real_time_doorkomsten[0].links[0].rel == "halte"
        assert (
            real_time_doorkomsten[0].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/haltes/4/403022"
        )


def test_storingen():
    response.status_code = 200
    response.reason = "OK"
    storingen_path = Path("tests/kern_open_data_services_api/v1/inputs/storingen.json")
    with storingen_path.open() as storingen_file:
        storingen = storingen_file.read()
    response._content = storingen.encode()
    with mock.patch("requests.request", return_value=response):
        storingen = get_storingen(4, 403022)
        assert (
            storingen[0].omschrijving
            == "Interventie hulpdiensten. Niet-bediende halte: Halle Colruyt."
        )
        assert storingen[0].lijnrichtingen[0].entiteitnummer == "3"
        assert storingen[0].lijnrichtingen[0].lijnnummer == "157"
        assert storingen[0].lijnrichtingen[0].richting == "TERUG"
        assert (
            storingen[0].lijnrichtingen[0].omschrijving == "Halle Don bosco - Lembeek"
        )
        assert storingen[0].lijnrichtingen[0].links[0].rel == "lijnrichting"
        assert (
            storingen[0].lijnrichtingen[0].links[0].url
            == "https://api.delijn.be/DLKernOpenData/api/v1/lijnen/3/157/lijnrichtingen/TERUG"
        )
