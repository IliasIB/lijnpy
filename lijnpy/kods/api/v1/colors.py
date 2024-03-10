from pydantic import ValidationError

from lijnpy import _logger
from lijnpy.exceptions import DeLijnAPIException
from lijnpy.kods.api.v1 import _rest_adapter
from lijnpy.kods.api.v1.models import ColorResponse, ColorsResponse


def get_colors() -> ColorsResponse:
    """Get a list of all colors

    Returns:
        list[Color]: A list of all colors
    """
    result = _rest_adapter.get("/kleuren")
    try:
        assert result.data is not None
        colors = ColorsResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return colors


def get_color(color_code: str) -> ColorResponse:
    """Get a color by its code

    Args:
        color_code (str): The code of the color

    Returns:
        Color: The color with the given code
    """
    result = _rest_adapter.get(f"/kleuren/{color_code}")
    try:
        assert result.data is not None
        color = ColorResponse(**result.data)
    except (AssertionError, ValidationError) as e:
        _logger.error(f"Failed to parse the response from the API: {e}")
        raise DeLijnAPIException from e

    return color