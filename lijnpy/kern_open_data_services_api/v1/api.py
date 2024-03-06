from pydantic_core import ValidationError

from lijnpy import _logger
from lijnpy.exceptions import DeLijnAPIException
from lijnpy.kern_open_data_services_api.v1 import _rest_adapter
from lijnpy.models import Link


def get_endpoints() -> list[Link]:
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
