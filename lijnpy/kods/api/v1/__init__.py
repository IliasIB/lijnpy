from lijnpy import API_KEY, _logger
from lijnpy._rest_adapter import RestAdapter

_rest_adapter = RestAdapter(
    "api.delijn.be/DLKernOpenData/api",
    API_KEY,
    "v1",
    True,
    _logger,
)
