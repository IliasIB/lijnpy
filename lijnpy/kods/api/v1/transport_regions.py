from lijnpy._rest_adapter import parse_api_call
from lijnpy.kods.api.v1.models import (
    Line,
    LineList,
    TransportRegion,
    TransportRegionList,
)


def get_transport_regions() -> list[TransportRegion]:
    """Get a list of all transport regions

    Returns:
        list[TransportRegion]: A list of all transport regions
    """

    return parse_api_call(
        "/vervoerregios",
        TransportRegionList,
    ).transport_regions


def get_transport_region(transport_region_code: str) -> TransportRegion:
    """Get a transport region by code

    Args:
        transport_region_code (str): The code of the transport region

    Returns:
        TransportRegion: The transport region
    """

    return parse_api_call(
        f"/vervoerregios/{transport_region_code}",
        TransportRegion,
    )


def get_lines(transport_region_code: str) -> list[Line]:
    """Get a list of lines by transport region code

    Args:
        transport_region_code (str): The code of the transport region

    Returns:
        list[Line]: A list of lines
    """

    return parse_api_call(
        f"/vervoerregios/{transport_region_code}/lijnen",
        LineList,
    ).lines
