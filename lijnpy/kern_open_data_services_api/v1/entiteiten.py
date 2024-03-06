from pydantic import ValidationError

from lijnpy import _logger
from lijnpy.exceptions import DeLijnAPIException
from lijnpy.kern_open_data_services_api.v1 import _rest_adapter
from lijnpy.models import Entiteit, Gemeente, Halte, Lijn


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


def get_entiteit_by_entiteitnummer(entiteitnummer: str) -> Entiteit:
    """Get an entity by its number

    Args:
        entiteitnummer (str): The number of the entity

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


def get_gemeenten_by_entiteitsnummer(entiteitnummer: str) -> list[Gemeente]:
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


def __clean_halte(halte: dict) -> dict:
    """Clean the stop data

    Args:
        halte (dict): The stop data

    Returns:
        dict: The cleaned stop data
    """
    return {
        "entiteitnummer": halte["entiteitnummer"],
        "haltenummer": halte["haltenummer"],
        "omschrijving": halte["omschrijving"],
        "omschrijving_lang": halte["omschrijvingLang"],
        "taal": halte["taal"],
        "gemeentenummer": halte["gemeentenummer"],
        "omschrijving_gemeente": halte["omschrijvingGemeente"],
        "geo_coordinaat": halte["geoCoordinaat"],
        "halte_toegankelijkheden": halte["halteToegankelijkheden"],
        "hoofd_halte": halte["hoofdHalte"],
        "links": halte["links"],
    }


def get_haltes_by_entiteitsnummer(entiteitnummer: str) -> list[Halte]:
    """Get a list of stops in Belgium for a given entity

    Args:
        entiteitnummer (str): The number of the entity

    Returns:
        Haltes: A list of stops in Belgium for a given entity
    """
    result = _rest_adapter.get(f"/entiteiten/{entiteitnummer}/haltes")
    try:
        assert result.data is not None
        haltes = [Halte(**__clean_halte(halte)) for halte in result.data["haltes"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return haltes


def __clean_lijn(lijn: dict) -> dict:
    """Clean the line data

    Args:
        lijn (dict): The line data

    Returns:
        dict: The cleaned line data
    """
    return {
        "entiteitnummer": lijn["entiteitnummer"],
        "lijnnummer": lijn["lijnnummer"],
        "lijnnummer_publiek": lijn["lijnnummerPubliek"],
        "omschrijving": lijn["omschrijving"],
        "vervoer_regio_code": lijn["vervoerRegioCode"],
        "publiek": lijn["publiek"],
        "vervoertype": lijn["vervoertype"],
        "bedieningtype": lijn["bedieningtype"],
        "lijn_geldig_van": lijn["lijnGeldigVan"],
        "lijn_geldig_tot": lijn["lijnGeldigTot"],
        "links": lijn["links"],
    }


def get_lijnen_by_entiteitsnummer(entiteitsnummer: str) -> list[Lijn]:
    """Get a list of lines in Belgium for a given entity

    Args:
        entiteitsnummer (str): The number of the entity

    Returns:
        Lijnen: A list of lines in Belgium for a given entity
    """
    result = _rest_adapter.get(f"/entiteiten/{entiteitsnummer}/lijnen")
    try:
        assert result.data is not None
        lijnen = [Lijn(**__clean_lijn(lijn)) for lijn in result.data["lijnen"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return lijnen
