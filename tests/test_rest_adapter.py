from unittest import mock

import pytest
import requests

from lijnpy._rest_adapter import DeLijnAPIException, RestAdapter, Result

rest_adapter = RestAdapter()
response = requests.Response()


def test__do_good_request_returns_result():
    response.status_code = 200
    response.reason = "OK"
    response._content = "{}".encode()
    with mock.patch("requests.request", return_value=response):
        result = rest_adapter._do("GET", "")
        assert isinstance(result, Result)


def test__do_bad_json_raises_delijnapi_exception():
    bad_json = '{"some bad json": '
    response._content = bad_json.encode()
    with mock.patch("requests.request", return_value=response):
        with pytest.raises(DeLijnAPIException):
            rest_adapter._do("GET", "")
