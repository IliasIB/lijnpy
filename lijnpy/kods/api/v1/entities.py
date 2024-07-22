from lijnpy._rest_adapter import parse_api_call
from lijnpy.kods.api.v1.models import (
    Entity,
    EntityList,
    Line,
    LineList,
    Municipality,
    MunicipalityList,
    Stop,
    StopList,
)


def get_entities() -> list[Entity]:
    """Get a list of all entities

    Returns:
        list[Entity]: A list of all entities
    """
    return parse_api_call("/entiteiten", EntityList).entities


def get_entity(entity_number: int) -> Entity:
    """Get an entity by its number

    Args:
        entity_number (int): The number of the entity

    Returns:
        Entity: The entity with the given number
    """
    return parse_api_call(f"/entiteiten/{entity_number}", Entity)


def get_municipalities(entity_number: int) -> list[Municipality]:
    """Get a list of municipalities in Belgium for a given entity

    Args:
        entity_number (str): The number of the entity

    Returns:
        list[Municipality]: A list of municipalities in Belgium for a given entity
    """
    return parse_api_call(
        f"/entiteiten/{entity_number}/gemeenten", MunicipalityList
    ).municipalities


def get_stops(entity_number: int) -> list[Stop]:
    """Get a list of stops in Belgium for a given entity

    Args:
        entity_number (str): The number of the entity

    Returns:
        list[Stop]: A list of stops in Belgium for a given entity
    """

    return parse_api_call(f"/entiteiten/{entity_number}/haltes", StopList).stops


def get_lines(entity_number: int) -> list[Line]:
    """Get a list of lines in Belgium for a given entity

    Args:
        entity_number (str): The number of the entity

    Returns:
        list[Line]: A list of lines in Belgium for a given entity
    """

    return parse_api_call(f"/entiteiten/{entity_number}/lijnen", LineList).lines
