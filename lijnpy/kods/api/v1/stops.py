from pydantic_core import ValidationError

from lijnpy import _logger
from lijnpy.kods.api.v1 import _rest_adapter
from lijnpy.kods.api.v1.models.stops import (
    DetoursResponse,
    DirectionsResponse,
    DisruptionsResponse,
    RealTimePassagesResponse,
    StopResponse,
    StopsInVicinityResponse,
    TimetableResponse,
)
from lijnpy.kods.api.v1.models.utils import GeoCoordinate
from lijnpy.rest_adapter import DeLijnAPIException


def get_stops_in_vicinity(
    geo_coordinate: GeoCoordinate,
) -> StopsInVicinityResponse:
    """Get a list of all available stops in the neighbourhood of the given geo-coordinates

    Args:
        geo_coordinate (GeoCoordinate): The geo-coordinates to search around

    Returns:
        StopsInVicinityResponse: A list of all available stops in the neighbourhood of the given geo-coordinates

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(
        f"/haltes/indebuurt/{geo_coordinate.latitude},{geo_coordinate.longitude}",
    )
    try:
        assert result.data is not None
        stops_in_vicinity_response = StopsInVicinityResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return stops_in_vicinity_response


def get_stop(entity_number: int, stop_number: int) -> StopResponse:
    """Get the stop with the given entity and stop number

    Args:
        entity_number (int): The number of the entity
        stop_number (int): The number of the stop

    Returns:
        StopResponse: The stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(f"/haltes/{entity_number}/{stop_number}")
    try:
        assert result.data is not None
        stop = StopResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return stop


def get_timetable(entity_number: int, stop_number: int) -> TimetableResponse:
    """Get the schedule of the stop with the given entity and stop number

    Returns:
        Timetable: The schedule of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(
        f"/haltes/{entity_number}/{stop_number}/dienstregelingen"
    )
    try:
        assert result.data is not None
        timetable_response = TimetableResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return timetable_response


def get_directions(entity_number: int, stop_number: int) -> DirectionsResponse:
    """Get the directions of the stop with the given entity and stop number

    Args:
        entity_number (int): The number of the entity
        stop_number (int): The number of the stop

    Returns:
        DirectionsResponse: The directions of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(f"/haltes/{entity_number}/{stop_number}/lijnrichtingen")
    try:
        assert result.data is not None
        directions_response = DirectionsResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return directions_response


def get_detours(entity_number: int, stop_number: int) -> DetoursResponse:
    """Get the detours of the stop with the given entity and stop number

    Args:
        entity_number (int): The number of the entity
        stop_number (int): The number of the stop

    Returns:
        DetoursResponse: The detours of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(f"/haltes/{entity_number}/{stop_number}/omleidingen")
    try:
        assert result.data is not None
        detours_response = DetoursResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return detours_response


def get_real_time_passages(
    entity_number: int, stop_number: int
) -> RealTimePassagesResponse:
    """Get the real-time arrivals of the stop with the given entity and stop number

    Args:
        entity_number (int): The number of the entity
        stop_number (int): The number of the stop

    Returns:
        RealTimePassagesResponse: The real-time arrivals of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(
        f"/haltes/{entity_number}/{stop_number}/real-time-doorkomsten"
    )
    try:
        assert result.data is not None
        real_time_passages = RealTimePassagesResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return real_time_passages


def get_disruptions(entity_number: int, stop_number: int) -> DisruptionsResponse:
    """Get the directions of the stop with the given entity and stop number

    Args:
        entity_number (int): The number of the entity
        stop_number (int): The number of the stop

    Returns:
        DisruptionsResponse: The disruptions of the stop with the given entity and stop number
    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(f"/haltes/{entity_number}/{stop_number}/storingen")
    try:
        assert result.data is not None
        disruptions_response = DisruptionsResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return disruptions_response
