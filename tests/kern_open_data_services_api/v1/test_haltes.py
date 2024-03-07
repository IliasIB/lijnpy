from unittest import mock

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
from lijnpy.models import GeoCoordinate
from tests.utils import get_good_request_input


def test_haltes():
    response = get_good_request_input(
        "tests/kern_open_data_services_api/v1/inputs/haltes.json"
    )
    with mock.patch("requests.request", return_value=response):
        haltes = get_haltes()
        assert haltes[0].entiteitnummer == 1
        assert haltes[0].haltenummer == 100118
        assert haltes[0].omschrijving == "Station"
        assert haltes[0].omschrijving_lang == "Bornem Station"
        assert haltes[0].gemeentenummer == 1350
        assert haltes[0].omschrijving_gemeente == "Bornem"
        assert haltes[0].geo_coordinaat.latitude == 51.099532
        assert haltes[0].geo_coordinaat.longitude == 4.240739
        assert haltes[0].halte_toegankelijkheden == []
        assert haltes[0].hoofd_halte is None
        assert haltes[0].taal == "?"


def test_haltes_in_neighbourhood():
    response = get_good_request_input(
        "tests/kern_open_data_services_api/v1/inputs/haltes_indebuurt.json"
    )
    with mock.patch("requests.request", return_value=response):
        haltes = get_haltes_in_neighbourhood(
            GeoCoordinate(latitude=51.004652, longitude=5.346613)
        )
        assert haltes[0].type == "DELIJN"
        assert haltes[0].id == 403022
        assert haltes[0].naam == "Zonhoven Hulsbergweg"
        assert haltes[0].afstand == 0
        assert haltes[0].geo_coordinate.latitude == 51.004652
        assert haltes[0].geo_coordinate.longitude == 5.346613


def test_halte():
    response = get_good_request_input(
        "tests/kern_open_data_services_api/v1/inputs/halte.json"
    )
    with mock.patch("requests.request", return_value=response):
        halte = get_halte("4", "403022")
        assert halte.entiteitnummer == 4
        assert halte.haltenummer == 403022
        assert halte.omschrijving == "Hulsbergweg"
        assert halte.omschrijving_lang == "Zonhoven Hulsbergweg"
        assert halte.gemeentenummer == 1588
        assert halte.omschrijving_gemeente == "Zonhoven"
        assert halte.geo_coordinaat.latitude == 51.004652
        assert halte.geo_coordinaat.longitude == 5.346613
        assert halte.halte_toegankelijkheden == []
        assert halte.hoofd_halte is None
        assert halte.taal == "?"


def test_dienstregelingen():
    response = get_good_request_input(
        "tests/kern_open_data_services_api/v1/inputs/dienstregeling.json"
    )
    with mock.patch("requests.request", return_value=response):
        dienstregeling = get_dienstregelingen("4", "403022")
        assert dienstregeling.doorkomsten[0].entiteitnummer == 4
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
    response = get_good_request_input(
        "tests/kern_open_data_services_api/v1/inputs/richtingen.json"
    )
    with mock.patch("requests.request", return_value=response):
        richtingen = get_richtingen(4, 403022)
        assert richtingen[0].entiteitnummer == 4
        assert richtingen[0].lijnnummer == 465
        assert richtingen[0].richting == "TERUG"
        assert richtingen[0].omschrijving == "Genk - Houthalen"
        assert richtingen[1].entiteitnummer == 4
        assert richtingen[1].lijnnummer == 950
        assert richtingen[1].richting == "HEEN"
        assert richtingen[1].omschrijving == "Regio Limburg"


def test_omleidingen():
    response = get_good_request_input(
        "tests/kern_open_data_services_api/v1/inputs/omleidingen.json"
    )
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


def test_real_time_doorkomsten():
    response = get_good_request_input(
        "tests/kern_open_data_services_api/v1/inputs/realtime.json"
    )
    with mock.patch("requests.request", return_value=response):
        real_time_doorkomsten = get_real_time_doorkomsten(4, 403022)
        assert real_time_doorkomsten[0].entiteitnummer == 4
        assert real_time_doorkomsten[0].lijnnummer == 465
        assert real_time_doorkomsten[0].richting == "TERUG"
        assert real_time_doorkomsten[0].ritnummer == 16
        assert real_time_doorkomsten[0].bestemming == "Houthalen"
        assert real_time_doorkomsten[0].vias == []
        assert real_time_doorkomsten[0].dienstregeling_tijdstip == "2024-03-07T17:05:00"
        assert real_time_doorkomsten[0].real_time_tijdstip == "2024-03-07T17:05:20"
        assert real_time_doorkomsten[0].vrtnum == 442079
        assert real_time_doorkomsten[0].prediction_statussen == ["REALTIME"]


def test_storingen():
    response = get_good_request_input(
        "tests/kern_open_data_services_api/v1/inputs/storingen.json"
    )
    with mock.patch("requests.request", return_value=response):
        storingen = get_storingen(4, 403022)
        assert (
            storingen[0].omschrijving
            == "Interventie hulpdiensten. Niet-bediende halte: Halle Colruyt."
        )
        assert storingen[0].lijnrichtingen[0].entiteitnummer == 3
        assert storingen[0].lijnrichtingen[0].lijnnummer == 157
        assert storingen[0].lijnrichtingen[0].richting == "TERUG"
        assert (
            storingen[0].lijnrichtingen[0].omschrijving == "Halle Don bosco - Lembeek"
        )
