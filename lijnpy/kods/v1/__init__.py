import os

from lijnpy import _logger
from lijnpy.rest_adapter import RestAdapter

_rest_adapter = RestAdapter(
    "api.delijn.be/DLKernOpenData/api",
    os.environ["DELIJN_API_KEY"],
    "v1",
    True,
    _logger,
)
