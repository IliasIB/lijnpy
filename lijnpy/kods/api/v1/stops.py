from lijnpy._rest_adapter import parse_api_call
from lijnpy.kods.api.v1.models import (
    Detour,
    DetourList,
    Direction,
    DirectionList,
    Disruption,
    DisruptionList,
    GeoCoordinate,
    RealTimeTimetable,
    Stop,
    StopInVicinity,
    StopInVicinityList,
    Timetable,
)


def get_stops_in_vicinity(
    geo_coordinate: GeoCoordinate,
) -> list[StopInVicinity]:
    """Get a list of all available stops in the neighbourhood of the given geo-coordinates

    Args:
        geo_coordinate (GeoCoordinate): The geo-coordinates to search around

    Returns:
        list[StopInVicinity]: A list of all available stops in the neighbourhood of the given geo-coordinates

    Raises:
        DeLijnAPIException: If the API request fails
    """

    return parse_api_call(
        f"/haltes/indebuurt/{geo_coordinate.latitude},{geo_coordinate.longitude}",
        StopInVicinityList,
    ).stops


def get_stop(entity_number: int, stop_number: int) -> Stop:
    """Get the stop with the given entity and stop number

    Args:
        entity_number (int): The number of the entity
        stop_number (int): The number of the stop

    Returns:
        Stop: The stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """

    return parse_api_call(
        f"/haltes/{entity_number}/{stop_number}",
        Stop,
    )


def get_timetable(entity_number: int, stop_number: int) -> Timetable:
    """Get the schedule of the stop with the given entity and stop number

    Returns:
        Timetable: The schedule of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """

    return parse_api_call(
        f"/haltes/{entity_number}/{stop_number}/dienstregelingen",
        Timetable,
    )


def get_directions(entity_number: int, stop_number: int) -> list[Direction]:
    """Get the directions of the stop with the given entity and stop number

    Args:
        entity_number (int): The number of the entity
        stop_number (int): The number of the stop

    Returns:
        list[Direction]: The directions of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """

    return parse_api_call(
        f"/haltes/{entity_number}/{stop_number}/lijnrichtingen",
        DirectionList,
    ).directions


def get_detours(entity_number: int, stop_number: int) -> list[Detour]:
    """Get the detours of the stop with the given entity and stop number

    Args:
        entity_number (int): The number of the entity
        stop_number (int): The number of the stop

    Returns:
        list[Detour]: The detours of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """

    return parse_api_call(
        f"/haltes/{entity_number}/{stop_number}/omleidingen",
        DetourList,
    ).detours


def get_real_time_timetable(entity_number: int, stop_number: int) -> RealTimeTimetable:
    """Get the real-time arrivals of the stop with the given entity and stop number

    Args:
        entity_number (int): The number of the entity
        stop_number (int): The number of the stop

    Returns:
        RealTimeTimetable: The real-time arrivals of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """

    return parse_api_call(
        f"/haltes/{entity_number}/{stop_number}/real-time-doorkomsten",
        RealTimeTimetable,
    )


def get_disruptions(entity_number: int, stop_number: int) -> list[Disruption]:
    """Get the directions of the stop with the given entity and stop number

    Args:
        entity_number (int): The number of the entity
        stop_number (int): The number of the stop

    Returns:
        list[Disruption]: The disruptions of the stop with the given entity and stop number
    Raises:
        DeLijnAPIException: If the API request fails
    """

    return parse_api_call(
        f"/haltes/{entity_number}/{stop_number}/storingen",
        DisruptionList,
    ).disruptions
