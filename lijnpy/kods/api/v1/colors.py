from lijnpy._rest_adapter import parse_api_call
from lijnpy.kods.api.v1.models import LineColor, LineColorList


def get_colors() -> list[LineColor]:
    """Get a list of all colors

    Returns:
        list[LineColor]: A list of all colors
    """

    return parse_api_call("/kleuren", LineColorList).colors


def get_color(color_code: str) -> LineColor:
    """Get a color by its code

    Args:
        color_code (str): The code of the color

    Returns:
        LineColor: The color with the given code
    """

    return parse_api_call(f"/kleuren/{color_code}", LineColor)
