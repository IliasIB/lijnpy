from pydantic import ValidationError

from lijnpy import _logger
from lijnpy.exceptions import DeLijnAPIException
from lijnpy.kern_open_data_services_api.v1 import _rest_adapter
from lijnpy.kern_open_data_services_api.v1.models import Gemeente, Halte, Lijn


def get_gemeenten() -> list[Gemeente]:
    """Get a list of all municipalities in Belgium

    Returns:
        Gemeenten: A list of all municipalities in Belgium
    """
    result = _rest_adapter.get("/gemeenten")
    try:
        assert result.data is not None
        gemeenten = [Gemeente(**link) for link in result.data["gemeenten"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return gemeenten


def get_haltes_by_gemeentenummers(gemeentenummers: list[int]) -> list[Halte]:
    """Get a list of all municipalities in Belgium

    Returns:
        Gemeenten: A list of all municipalities in Belgium
    """
    gemeentenummer_strings = ",".join(
        str(gemeentenummer) for gemeentenummer in gemeentenummers
    )
    result = _rest_adapter.get(f"/gemeenten/lijst/{gemeentenummer_strings}/haltes")
    try:
        assert result.data is not None
        haltes = [
            Halte(**halte)
            for gemeentehalte in result.data["gemeenteHaltes"]
            for halte in gemeentehalte["haltes"]
        ]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return haltes


def get_haltes_by_gemeentenummer(gemeentenummer: int) -> list[Halte]:
    """Get a list of stops in a municipality

    Args:
        gemeentenummer (int): The municipality number

    Returns:
        list[Halte]: A list of stops in the municipality
    """
    result = _rest_adapter.get(f"/gemeenten/{gemeentenummer}/haltes")
    try:
        assert result.data is not None
        haltes = [Halte(**halte) for halte in result.data["haltes"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return haltes


def get_lijnen_by_gemeentenummer(gemeentenummer: int) -> list[Lijn]:
    """Get a list of lines in a municipality

    Args:
        gemeentenummer (int): The municipality number

    Returns:
        list[Lijn]: A list of lines in the municipality
    """
    result = _rest_adapter.get(f"/gemeenten/{gemeentenummer}/lijnen")
    try:
        assert result.data is not None
        lijnen = [Lijn(**lijn) for lijn in result.data["lijnen"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return lijnen


def get_gemeente_by_gemeentenummer(gemeentenummer: int) -> Gemeente:
    """Get a municipality by its number

    Args:
        gemeentenummer (int): The number of the municipality

    Returns:
        Gemeente: The municipality with the given number
    """
    result = _rest_adapter.get(f"/gemeenten/{gemeentenummer}")
    try:
        assert result.data is not None
        gemeente = Gemeente(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return gemeente
