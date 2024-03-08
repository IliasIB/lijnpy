from unittest import mock

from lijnpy.kern_open_data_services_api.v1.models import GeoCoordinate
from lijnpy.kern_open_data_services_api.v1.stops import (
    get_detours,
    get_directions,
    get_disruptions,
    get_real_time_passages,
    get_stop,
    get_stops,
    get_stops_in_vicinity,
    get_timetable,
)
from tests.utils import input_as_response


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/haltes.json"
    ),
)
def test_stops(_):
    haltes = get_stops()
    assert len(haltes) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/haltes_indebuurt.json"
    ),
)
def test_stops_in_vicinity(_):
    haltes = get_stops_in_vicinity(
        GeoCoordinate(latitude=51.004652, longitude=5.346613)
    )
    assert len(haltes) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/halte.json"
    ),
)
def test_stop(_):
    halte = get_stop("4", "403022")
    assert halte.entity_number == 4
    assert halte.number == 403022
    assert halte.description == "Hulsbergweg"
    assert halte.description_long == "Zonhoven Hulsbergweg"
    assert halte.municipality_number == 1588
    assert halte.omschrijving_gemeente == "Zonhoven"
    assert halte.geo_coordinate.latitude == 51.004652
    assert halte.geo_coordinate.longitude == 5.346613
    assert halte.accessibilities == []
    assert halte.is_main is None
    assert halte.language == "?"


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/dienstregeling.json"
    ),
)
def test_timetable(_):
    dienstregeling = get_timetable(4, 403022)
    assert len(dienstregeling.passages) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/richtingen.json"
    ),
)
def test_directions(_):
    richtingen = get_directions(4, 403022)
    assert len(richtingen) == 2


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/omleidingen.json"
    ),
)
def test_detours(_):
    omleidingen = get_detours(4, 403022)
    assert len(omleidingen) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/realtime.json"
    ),
)
def test_real_time_passages(_):
    real_time_doorkomsten = get_real_time_passages(4, 403022)
    assert len(real_time_doorkomsten) == 1


@mock.patch(
    "requests.request",
    return_value=input_as_response(
        "tests/kern_open_data_services_api/v1/inputs/storingen.json"
    ),
)
def test_disruption(_):
    storingen = get_disruptions(4, 403022)
    assert len(storingen) == 1
