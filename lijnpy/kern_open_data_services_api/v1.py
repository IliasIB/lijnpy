import os
from logging import getLogger

from pydantic import ValidationError

from lijnpy.exceptions import DeLijnAPIException
from lijnpy.models import Gemeenten, Link
from lijnpy.rest_adapter import RestAdapter

_logger = getLogger(__name__)
_rest_adapter = RestAdapter(
    "api.delijn.be/DLKernOpenData/api",
    os.environ["DELIJN_API_KEY"],
    "v1",
    True,
    _logger,
)


def get_gemeenten() -> Gemeenten:
    """Get a list of all municipalities in Belgium

    Returns:
        Gemeenten: A list of all municipalities in Belgium
    """
    result = _rest_adapter.get("/gemeenten")
    try:
        assert result.data is not None
        gemeenten = Gemeenten(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return gemeenten


def get_api() -> list[Link]:
    """Get a list of all available API endpoints

    Returns:
        list[Link]: A list of all available API endpoints
    """
    result = _rest_adapter.get("/api")
    try:
        assert result.data is not None
        links = [Link(**link) for link in result.data["links"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return links
