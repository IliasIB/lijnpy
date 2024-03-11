from pydantic import ValidationError

from lijnpy import _logger
from lijnpy.exceptions import DeLijnAPIException
from lijnpy.kods.api.v1 import _rest_adapter
from lijnpy.kods.api.v1.models.transport_regions import (
    LinesResponse,
    TransportRegionResponse,
    TransportRegionsResponse,
)


def get_transport_regions() -> TransportRegionsResponse:
    """Get a list of all transport regions

    Returns:
        TransportRegionsResponse: A list of all transport regions
    """
    result = _rest_adapter.get("/vervoerregios")
    try:
        assert result.data is not None
        transport_regions = TransportRegionsResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return transport_regions


def get_transport_region(transport_region_code: str) -> TransportRegionResponse:
    """Get a transport region by code

    Args:
        transport_region_code (str): The code of the transport region

    Returns:
        TransportRegion: The transport region
    """
    result = _rest_adapter.get(f"/vervoerregios/{transport_region_code}")
    try:
        assert result.data is not None
        transport_region = TransportRegionResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return transport_region


def get_lines(transport_region_code: str) -> LinesResponse:
    """Get a list of lines by transport region code

    Args:
        transport_region_code (str): The code of the transport region

    Returns:
        LinesResponse: A list of lines
    """
    result = _rest_adapter.get(f"/vervoerregios/{transport_region_code}/lijnen")
    try:
        assert result.data is not None
        lines_response = LinesResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return lines_response
