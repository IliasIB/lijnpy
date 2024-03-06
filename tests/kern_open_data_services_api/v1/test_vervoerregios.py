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
