from pydantic import ValidationError

from lijnpy import _logger
from lijnpy.exceptions import DeLijnAPIException
from lijnpy.kods.api.v1 import _rest_adapter
from lijnpy.kods.api.v1.models import (
    LinesResponse,
    MunicipalitiesResponse,
    MunicipalityResponse,
    StopsResponse,
)


def get_municipalities() -> MunicipalitiesResponse:
    """Get a list of all municipalities in Belgium

    Returns:
        MunicipalitiesResponse: A list of all municipalities in Belgium
    """
    result = _rest_adapter.get("/gemeenten")
    try:
        assert result.data is not None
        municipalities_response = MunicipalitiesResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return municipalities_response


def get_stops(municipality_number: int) -> StopsResponse:
    """Get a list of stops in a municipality

    Args:
        municipality_number (int): The municipality number

    Returns:
        StopsResponse: A list of stops in the municipality
    """
    result = _rest_adapter.get(f"/gemeenten/{municipality_number}/haltes")
    try:
        assert result.data is not None
        stops_response = StopsResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return stops_response


def get_lines(municipality_number: int) -> LinesResponse:
    """Get a list of lines in a municipality

    Args:
        municipality_number (int): The municipality number

    Returns:
        LinesResponse: A list of lines in the municipality
    """
    result = _rest_adapter.get(f"/gemeenten/{municipality_number}/lijnen")
    try:
        assert result.data is not None
        lines_response = LinesResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return lines_response


def get_municipality(municipality_number: int) -> MunicipalityResponse:
    """Get a municipality by its number

    Args:
        municipality_number (int): The number of the municipality

    Returns:
        Municipality: The municipality with the given number
    """
    result = _rest_adapter.get(f"/gemeenten/{municipality_number}")
    try:
        assert result.data is not None
        municipality = MunicipalityResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return municipality
