from pydantic import ValidationError

from lijnpy import _logger
from lijnpy.exceptions import DeLijnAPIException
from lijnpy.kern_open_data_services_api.v1 import _rest_adapter
from lijnpy.models import Vervoerregio


def get_vervoerregios() -> list[Vervoerregio]:
    """Get a list of all transport regions

    Returns:
        list[Vervoerregio]: A list of all transport regions
    """
    result = _rest_adapter.get("/vervoerregios")
    try:
        assert result.data is not None
        vervoerregios = [
            Vervoerregio(**vervoerregio)
            for vervoerregio in result.data["vervoerRegios"]
        ]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return vervoerregios


def get_vervoerregio_by_code(code: str) -> Vervoerregio:
    """Get a transport region by code

    Args:
        code (str): The code of the transport region

    Returns:
        Vervoerregio: The transport region
    """
    result = _rest_adapter.get(f"/vervoerregios/{code}")
    try:
        assert result.data is not None
        vervoerregio = Vervoerregio(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return vervoerregio
