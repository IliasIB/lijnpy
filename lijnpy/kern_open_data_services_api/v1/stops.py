from pydantic_core import ValidationError

from lijnpy import _logger
from lijnpy.exceptions import DeLijnAPIException
from lijnpy.kern_open_data_services_api.v1 import _rest_adapter
from lijnpy.kern_open_data_services_api.v1.models import (
    Detour,
    Direction,
    Disruption,
    GeoCoordinate,
    RealTimePassage,
    Stop,
    StopInVicinity,
    Timetable,
)


def get_stops() -> list[Stop]:
    """Get a list of all available stops

    Returns:
        Stops: A list of all available stops

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get("/haltes")
    try:
        assert result.data is not None
        stops = [Stop(**stop) for stop in result.data["haltes"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return stops


def get_stops_in_vicinity(geo_coordinate: GeoCoordinate) -> list[StopInVicinity]:
    """Get a list of all available stops in the neighbourhood of the given geo-coordinates

    Args:
        geo_coordinate (GeoCoordinate): The geo-coordinates to search around

    Returns:
        Stops: A list of all available stops in the neighbourhood of the given geo-coordinates

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(
        f"/haltes/indebuurt/{geo_coordinate.latitude},{geo_coordinate.longitude}",
    )
    try:
        assert result.data is not None
        stops = [StopInVicinity(**stop) for stop in result.data["haltes"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return stops


def get_stop(entity_number: str, stop_number: str) -> Stop:
    """Get the stop with the given entity and stop number

    Args:
        entity_number (str): The number of the entity
        stop_number (str): The number of the stop

    Returns:
        Stop: The stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(f"/haltes/{entity_number}/{stop_number}")
    try:
        assert result.data is not None
        stop = Stop(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return stop


def get_timetable(entity_number: int, stop_number: int) -> Timetable:
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
        timetable = {
            "doorkomsten": [
                passage
                for stop_passages in result.data["halteDoorkomsten"]
                for passage in stop_passages["doorkomsten"]
            ],
            "doorkomstNotas": result.data["doorkomstNotas"],
            "ritNotas": result.data["ritNotas"],
        }
        timetable = Timetable(**timetable)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return timetable


def get_directions(entity_number: int, stop_number: int) -> list[Direction]:
    """Get the directions of the stop with the given entity and stop number

    Args:
        entity_number (int): The number of the entity
        stop_number (int): The number of the stop

    Returns:
        Directions: The directions of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(f"/haltes/{entity_number}/{stop_number}/lijnrichtingen")
    try:
        assert result.data is not None
        directions = [
            Direction(**direction) for direction in result.data["lijnrichtingen"]
        ]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return directions


def get_detours(entity_number: int, stop_number: int) -> list[Detour]:
    """Get the directions of the stop with the given entity and stop number

    Args:
        entity_number (int): The number of the entity
        stop_number (int): The number of the stop

    Returns:
        list[Richting]: The directions of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(f"/haltes/{entity_number}/{stop_number}/omleidingen")
    try:
        assert result.data is not None
        detours = [Detour(**detour) for detour in result.data["omleidingen"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return detours


def get_real_time_passages(
    entity_number: int, stop_number: int
) -> list[RealTimePassage]:
    """Get the real-time arrivals of the stop with the given entity and stop number

    Args:
        entity_number (int): The number of the entity
        stop_number (int): The number of the stop

    Returns:
        RealTimePassages: The real-time arrivals of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(
        f"/haltes/{entity_number}/{stop_number}/real-time-doorkomsten"
    )
    try:
        assert result.data is not None
        real_time_passages = [
            RealTimePassage(**real_time_passage)
            for stop_passage in result.data["halteDoorkomsten"]
            for real_time_passage in stop_passage["doorkomsten"]
        ]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return real_time_passages


def get_disruptions(entity_number: int, stop_number: int) -> list[Disruption]:
    """Get the directions of the stop with the given entity and stop number

    Args:
        entity_number (int): The number of the entity
        stop_number (int): The number of the stop

    Returns:
        Disruption: The disruptions of the stop with the given entity and stop number
    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(f"/haltes/{entity_number}/{stop_number}/storingen")
    try:
        assert result.data is not None
        disruptions = [
            Disruption(**disruption) for disruption in result.data["storingen"]
        ]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return disruptions
