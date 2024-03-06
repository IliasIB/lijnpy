import json
from unittest import mock

import requests

from lijnpy.kern_open_data_services_api.v1.gemeenten import get_gemeenten

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
