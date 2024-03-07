from pydantic_core import ValidationError

from lijnpy import _logger
from lijnpy.exceptions import DeLijnAPIException
from lijnpy.kern_open_data_services_api.v1 import _rest_adapter
from lijnpy.kern_open_data_services_api.v1.models import (
    Dienstregeling,
    Doorkomst,
    DoorkomstNota,
    GeoCoordinate,
    Halte,
    HalteInDeBuurt,
    Omleiding,
    RealTimeDoorkomst,
    Richting,
    RitNota,
    Storing,
)
from lijnpy.utils import clean_doorkomst, clean_halte, clean_halte_in_de_buurt


def get_haltes() -> list[Halte]:
    """Get a list of all available stops

    Returns:
        list[Halte]: A list of all available stops

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get("/haltes")
    try:
        assert result.data is not None
        haltes = [Halte(**clean_halte(halte)) for halte in result.data["haltes"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return haltes


def get_haltes_in_neighbourhood(geo_coordinaat: GeoCoordinate) -> list[HalteInDeBuurt]:
    """Get a list of all available stops in the neighbourhood of the given geo-coordinates

    Args:
        geo_coordinaat (GeoCoordinaat): The geo-coordinates to search around

    Returns:
        list[Halte]: A list of all available stops in the neighbourhood of the given geo-coordinates

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(
        f"/haltes/indebuurt/{geo_coordinaat.latitude},{geo_coordinaat.longitude}",
    )
    try:
        assert result.data is not None
        haltes = [
            HalteInDeBuurt(**clean_halte_in_de_buurt(halte))
            for halte in result.data["haltes"]
        ]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return haltes


def get_halte(entiteitnummer: str, haltenummer: str) -> Halte:
    """Get the stop with the given entity and stop number

    Args:
        entiteitnummer (str): The number of the entity
        haltenummer (str): The number of the stop

    Returns:
        Halte: The stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(f"/haltes/{entiteitnummer}/{haltenummer}")
    try:
        assert result.data is not None
        halte = Halte(**clean_halte(result.data))
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return halte


# TODO: make parameters into ints
def get_dienstregelingen(entiteitnummer: str, haltenummer: str) -> Dienstregeling:
    """Get the schedule of the stop with the given entity and stop number

    Returns:
        Dienstregeling: The schedule of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(
        f"/haltes/{entiteitnummer}/{haltenummer}/dienstregelingen"
    )
    try:
        assert result.data is not None
        dienstregeling = Dienstregeling(
            doorkomsten=[
                Doorkomst(**clean_doorkomst(doorkomst))
                for halte_doorkomsten in result.data["halteDoorkomsten"]
                for doorkomst in halte_doorkomsten["doorkomsten"]
            ],
            doorkomst_notas=[
                DoorkomstNota(**doorkomst_nota)
                for doorkomst_nota in result.data["doorkomstNotas"]
            ],
            rit_notas=[RitNota(**rit_nota) for rit_nota in result.data["ritNotas"]],
        )
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return dienstregeling


def get_richtingen(entiteitnummer: int, haltenummer: int) -> list[Richting]:
    """Get the directions of the stop with the given entity and stop number

    Args:
        entiteitnummer (int): The number of the entity
        haltenummer (int): The number of the stop

    Returns:
        list[Richting]: The directions of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(f"/haltes/{entiteitnummer}/{haltenummer}/lijnrichtingen")
    try:
        assert result.data is not None
        richtingen = [
            Richting(**richting) for richting in result.data["lijnrichtingen"]
        ]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return richtingen


def get_omleidingen(entiteitnummer: int, haltenummer: int) -> list[Omleiding]:
    """Get the directions of the stop with the given entity and stop number

    Args:
        entiteitnummer (int): The number of the entity
        haltenummer (int): The number of the stop

    Returns:
        list[Richting]: The directions of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(f"/haltes/{entiteitnummer}/{haltenummer}/omleidingen")
    try:
        assert result.data is not None
        omleidingen = [
            Omleiding(**omleiding) for omleiding in result.data["omleidingen"]
        ]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return omleidingen


def get_real_time_doorkomsten(
    entiteitnummer: int, haltenummer: int
) -> list[RealTimeDoorkomst]:
    """Get the real-time arrivals of the stop with the given entity and stop number

    Args:
        entiteitnummer (int): The number of the entity
        haltenummer (int): The number of the stop

    Returns:
        list[RealTimeDoorkomst]: The real-time arrivals of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(
        f"/haltes/{entiteitnummer}/{haltenummer}/real-time-doorkomsten"
    )
    try:
        assert result.data is not None
        real_time_doorkomsten = [
            RealTimeDoorkomst(**real_time_doorkomst)
            for halteDoorkomst in result.data["halteDoorkomsten"]
            for real_time_doorkomst in halteDoorkomst["doorkomsten"]
        ]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return real_time_doorkomsten


def get_storingen(entiteitnummer: int, haltenummer: int) -> list[Storing]:
    """Get the directions of the stop with the given entity and stop number

    Args:
        entiteitnummer (int): The number of the entity
        haltenummer (int): The number of the stop

    Returns:
        list[Richting]: The directions of the stop with the given entity and stop number

    Raises:
        DeLijnAPIException: If the API request fails
    """
    result = _rest_adapter.get(f"/haltes/{entiteitnummer}/{haltenummer}/storingen")
    try:
        assert result.data is not None
        storingen = [Storing(**storing) for storing in result.data["storingen"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return storingen
