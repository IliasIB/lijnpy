from pydantic import ValidationError

from lijnpy import _logger
from lijnpy.exceptions import DeLijnAPIException
from lijnpy.kern_open_data_services_api.v1 import _rest_adapter
from lijnpy.models import Gemeente


def get_gemeenten() -> list[Gemeente]:
    """Get a list of all municipalities in Belgium

    Returns:
        Gemeenten: A list of all municipalities in Belgium
    """
    result = _rest_adapter.get("/gemeenten")
    try:
        assert result.data is not None
        gemeenten = [Gemeente(**link) for link in result.data["gemeenten"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return gemeenten
