from lijnpy._rest_adapter import parse_api_call
from lijnpy.kods.api.v1.models import (
    Line,
    LineList,
    Municipality,
    MunicipalityList,
    Stop,
    StopList,
)


def get_municipalities() -> list[Municipality]:
    """Get a list of all municipalities in Belgium

    Returns:
        list[Municipality]: A list of all municipalities in Belgium
    """

    return parse_api_call("/gemeenten", MunicipalityList).municipalities


def get_stops(municipality_number: int) -> list[Stop]:
    """Get a list of stops in a municipality

    Args:
        municipality_number (int): The municipality number

    Returns:
        list[Stop]: A list of stops in the municipality
    """

    return parse_api_call(f"/gemeenten/{municipality_number}/haltes", StopList).stops


def get_lines(municipality_number: int) -> list[Line]:
    """Get a list of lines in a municipality

    Args:
        municipality_number (int): The municipality number

    Returns:
        list[Line]: A list of lines in the municipality
    """

    return parse_api_call(f"/gemeenten/{municipality_number}/lijnen", LineList).lines


def get_municipality(municipality_number: int) -> Municipality:
    """Get a municipality by its number

    Args:
        municipality_number (int): The number of the municipality

    Returns:
        Municipality: The municipality with the given number
    """

    return parse_api_call(f"/gemeenten/{municipality_number}", Municipality)
