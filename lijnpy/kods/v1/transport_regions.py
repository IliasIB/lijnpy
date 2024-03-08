from pydantic import ValidationError

from lijnpy import _logger
from lijnpy.exceptions import DeLijnAPIException
from lijnpy.kods.v1 import _rest_adapter
from lijnpy.kods.v1.models import Line, TransportRegion


def get_transport_regions() -> list[TransportRegion]:
    """Get a list of all transport regions

    Returns:
        list[TransportRegion]: A list of all transport regions
    """
    result = _rest_adapter.get("/vervoerregios")
    try:
        assert result.data is not None
        transport_regions = [
            TransportRegion(**transport_region)
            for transport_region in result.data["vervoerRegios"]
        ]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return transport_regions


def get_transport_region(transport_region_code: str) -> TransportRegion:
    """Get a transport region by code

    Args:
        transport_region_code (str): The code of the transport region

    Returns:
        TransportRegion: The transport region
    """
    result = _rest_adapter.get(f"/vervoerregios/{transport_region_code}")
    try:
        assert result.data is not None
        transport_region = TransportRegion(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return transport_region


def get_lines(transport_region_code: str) -> list[Line]:
    """Get a list of lines by transport region code

    Args:
        transport_region_code (str): The code of the transport region

    Returns:
        list[Line]: A list of lines
    """
    result = _rest_adapter.get(f"/vervoerregios/{transport_region_code}/lijnen")
    try:
        assert result.data is not None
        lines = [Line(**line) for line in result.data["lijnen"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return lines
