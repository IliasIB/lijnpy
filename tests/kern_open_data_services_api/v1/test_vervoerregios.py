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
