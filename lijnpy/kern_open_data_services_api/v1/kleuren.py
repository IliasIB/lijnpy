from pydantic import ValidationError

from lijnpy import _logger
from lijnpy.exceptions import DeLijnAPIException
from lijnpy.kern_open_data_services_api.v1 import _rest_adapter
from lijnpy.kern_open_data_services_api.v1.models import Kleur


def get_kleuren() -> list[Kleur]:
    """Get a list of all colors

    Returns:
        list[Kleur]: A list of all colors
    """
    result = _rest_adapter.get("/kleuren")
    try:
        assert result.data is not None
        kleuren = [Kleur(**kleur) for kleur in result.data["kleuren"]]
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return kleuren


def get_kleur_by_code(kleurcode: str) -> Kleur:
    """Get a color by its code

    Args:
        kleurcode (str): The code of the color

    Returns:
        Kleur: The color with the given code
    """
    result = _rest_adapter.get(f"/kleuren/{kleurcode}")
    try:
        assert result.data is not None
        kleur = Kleur(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return kleur
