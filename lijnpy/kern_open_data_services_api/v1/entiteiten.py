from pydantic import ValidationError

from lijnpy import _logger
from lijnpy.exceptions import DeLijnAPIException
from lijnpy.kern_open_data_services_api.v1 import _rest_adapter
from lijnpy.kern_open_data_services_api.v1.models import Entiteit, Gemeente, Halte, Lijn


def get_entiteiten() -> list[Entiteit]:
    """Get a list of all entities

    Returns:
        list[Entiteit]: A list of all entities
    """
    result = _rest_adapter.get("/entiteiten")
    try:
        assert result.data is not None
        entiteiten = [Entiteit(**entiteit) for entiteit in result.data["entiteiten"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return entiteiten


def get_entiteit_by_entiteitnummer(entiteitnummer: int) -> Entiteit:
    """Get an entity by its number

    Args:
        entiteitnummer (int): The number of the entity

    Returns:
        Entiteit: The entity with the given number
    """
    result = _rest_adapter.get(f"/entiteiten/{entiteitnummer}")
    try:
        assert result.data is not None
        entiteit = Entiteit(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return entiteit


def get_gemeenten_by_entiteitsnummer(entiteitnummer: int) -> list[Gemeente]:
    """Get a list of municipalities in Belgium for a given entity

    Args:
        entiteitnummer (str): The number of the entity

    Returns:
        Gemeenten: A list of municipalities in Belgium for a given entity
    """
    result = _rest_adapter.get(f"/entiteiten/{entiteitnummer}/gemeenten")
    try:
        assert result.data is not None
        gemeenten = [Gemeente(**gemeente) for gemeente in result.data["gemeenten"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return gemeenten


def get_haltes_by_entiteitsnummer(entiteitnummer: int) -> list[Halte]:
    """Get a list of stops in Belgium for a given entity

    Args:
        entiteitnummer (str): The number of the entity

    Returns:
        Haltes: A list of stops in Belgium for a given entity
    """
    result = _rest_adapter.get(f"/entiteiten/{entiteitnummer}/haltes")
    try:
        assert result.data is not None
        haltes = [Halte(**halte) for halte in result.data["haltes"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return haltes


def get_lijnen_by_entiteitsnummer(entiteitsnummer: int) -> list[Lijn]:
    """Get a list of lines in Belgium for a given entity

    Args:
        entiteitsnummer (str): The number of the entity

    Returns:
        Lijnen: A list of lines in Belgium for a given entity
    """
    result = _rest_adapter.get(f"/entiteiten/{entiteitsnummer}/lijnen")
    try:
        assert result.data is not None
        lijnen = [Lijn(**lijn) for lijn in result.data["lijnen"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return lijnen
