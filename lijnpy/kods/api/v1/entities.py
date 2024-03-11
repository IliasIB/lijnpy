from pydantic import ValidationError

from lijnpy import _logger
from lijnpy.exceptions import DeLijnAPIException
from lijnpy.kods.api.v1 import _rest_adapter
from lijnpy.kods.api.v1.models.entities import (
    EntitiesResponse,
    EntityResponse,
    LinesResponse,
    MunicipalitiesResponse,
    StopsResponse,
)


def get_entities() -> EntitiesResponse:
    """Get a list of all entities

    Returns:
        EntitiesResponse: A list of all entities
    """
    result = _rest_adapter.get("/entiteiten")
    try:
        assert result.data is not None
        entities_response = EntitiesResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return entities_response


def get_entity(entity_number: int) -> EntityResponse:
    """Get an entity by its number

    Args:
        entity_number (int): The number of the entity

    Returns:
        Entity: The entity with the given number
    """
    result = _rest_adapter.get(f"/entiteiten/{entity_number}")
    try:
        assert result.data is not None
        entity = EntityResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return entity


def get_municipalities(entity_number: int) -> MunicipalitiesResponse:
    """Get a list of municipalities in Belgium for a given entity

    Args:
        entity_number (str): The number of the entity

    Returns:
        MunicipalitiesResponse: A list of municipalities in Belgium for a given entity
    """
    result = _rest_adapter.get(f"/entiteiten/{entity_number}/gemeenten")
    try:
        assert result.data is not None
        municipalities_response = MunicipalitiesResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return municipalities_response


def get_stops(entity_number: int) -> StopsResponse:
    """Get a list of stops in Belgium for a given entity

    Args:
        entity_number (str): The number of the entity

    Returns:
        StopsResponse: A list of stops in Belgium for a given entity
    """
    result = _rest_adapter.get(f"/entiteiten/{entity_number}/haltes")
    try:
        assert result.data is not None
        stops_response = StopsResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return stops_response


def get_lines(entity_number: int) -> LinesResponse:
    """Get a list of lines in Belgium for a given entity

    Args:
        entity_number (str): The number of the entity

    Returns:
        LinesResponse: A list of lines in Belgium for a given entity
    """
    result = _rest_adapter.get(f"/entiteiten/{entity_number}/lijnen")
    try:
        assert result.data is not None
        lines_response = LinesResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return lines_response
