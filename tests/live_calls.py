"""One call per KODSClientV1 endpoint, shared by the recorder and the live tests.

Each entry maps a client method name to the fixture it is recorded into and a
factory that performs the call. The IDs below must exist in the live API.
"""

import os
from datetime import date
from collections.abc import Awaitable, Callable

from pydantic_extra_types.coordinate import Latitude, Longitude

from lijnpy.enums import LineDirection
from lijnpy.kods_client_v1 import KODSClientV1
from lijnpy.models import GeoCoordinate

API_KEY_VARIABLE = "DELIJN_API_KEY"

ENTITY = 1  # Antwerpen
STOP = 102675  # Antwerpen Groenplaats
MUNICIPALITY = 482  # Aalter (has stops and lines; municipality 1 has none)
REGION = "AN"  # Antwerpen transport region
COLOR = "TU"
LINE = 22  # Groenplaats - UZA, in entity 1
DIRECTION = LineDirection.TO
RIDE = 3  # a ride of line 22 in direction HEEN; the API needs the day for it
LINE_DIRECTIONS = [(ENTITY, LINE, LineDirection.TO), (ENTITY, LINE, LineDirection.FROM)]
LOCATION = GeoCoordinate(latitude=Latitude(51.2194), longitude=Longitude(4.4025))


def get_api_key() -> str | None:
    return os.environ.get(API_KEY_VARIABLE) or None


def get_calls(
    client: KODSClientV1,
) -> dict[str, tuple[str, Callable[[], Awaitable[object]]]]:
    """Method name -> (fixture file name, call)."""
    return {
        "get_colors": ("colors", lambda: client.get_colors()),
        "get_color": ("color", lambda: client.get_color(COLOR)),
        "get_entities": ("entities", lambda: client.get_entities()),
        "get_entity": ("entity", lambda: client.get_entity(ENTITY)),
        "get_municipalities_by_entity": (
            "municipalities_by_entity",
            lambda: client.get_municipalities_by_entity(ENTITY),
        ),
        "get_stops_by_entity": (
            "stops_by_entity",
            lambda: client.get_stops_by_entity(ENTITY),
        ),
        "get_lines_by_entity": (
            "lines_by_entity",
            lambda: client.get_lines_by_entity(ENTITY),
        ),
        "get_all_lines": ("lines", lambda: client.get_all_lines()),
        "get_line": ("line", lambda: client.get_line(ENTITY, LINE)),
        "get_municipalities_by_line": (
            "municipalities_by_line",
            lambda: client.get_municipalities_by_line(ENTITY, LINE),
        ),
        "get_line_colors": (
            "line_colors",
            lambda: client.get_line_colors(ENTITY, LINE),
        ),
        "get_line_directions": (
            "line_directions",
            lambda: client.get_line_directions(ENTITY, LINE),
        ),
        "get_line_direction": (
            "line_direction",
            lambda: client.get_line_direction(ENTITY, LINE, DIRECTION),
        ),
        "get_line_direction_timetable": (
            "line_direction_timetable",
            lambda: client.get_line_direction_timetable(ENTITY, LINE, DIRECTION),
        ),
        "get_line_direction_ride": (
            "line_direction_ride",
            lambda: client.get_line_direction_ride(
                ENTITY, LINE, DIRECTION, RIDE, day=date.today()
            ),
        ),
        "get_line_direction_stops": (
            "line_direction_stops",
            lambda: client.get_line_direction_stops(ENTITY, LINE, DIRECTION),
        ),
        "get_line_direction_detours": (
            "line_direction_detours",
            lambda: client.get_line_direction_detours(ENTITY, LINE, DIRECTION),
        ),
        "get_line_direction_real_time_timetable": (
            "line_direction_real_time_timetable",
            lambda: client.get_line_direction_real_time_timetable(
                ENTITY, LINE, DIRECTION
            ),
        ),
        "get_line_direction_disruptions": (
            "line_direction_disruptions",
            lambda: client.get_line_direction_disruptions(ENTITY, LINE, DIRECTION),
        ),
        "get_all_detours": (
            "all_detours",
            lambda: client.get_all_detours(start=date.today()),
        ),
        "get_detours_by_line_directions": (
            "detours_by_line_directions",
            lambda: client.get_detours_by_line_directions(LINE_DIRECTIONS),
        ),
        "get_disruptions_by_line_directions": (
            "disruptions_by_line_directions",
            lambda: client.get_disruptions_by_line_directions(LINE_DIRECTIONS),
        ),
        "get_municipalities": ("municipalities", lambda: client.get_municipalities()),
        "get_municipality": (
            "municipality",
            lambda: client.get_municipality(MUNICIPALITY),
        ),
        "get_stops": ("stops_by_municipality", lambda: client.get_stops(MUNICIPALITY)),
        "get_lines": (
            "lines_by_municipality",
            lambda: client.get_lines(MUNICIPALITY),
        ),
        "get_stops_in_vicinity": (
            "stops_in_vicinity",
            lambda: client.get_stops_in_vicinity(LOCATION),
        ),
        "get_stop": ("stop", lambda: client.get_stop(ENTITY, STOP)),
        "get_timetable": ("timetable", lambda: client.get_timetable(ENTITY, STOP)),
        "get_directions": ("directions", lambda: client.get_directions(ENTITY, STOP)),
        "get_detours": ("detours", lambda: client.get_detours(ENTITY, STOP)),
        "get_real_time_timetable": (
            "real_time_timetable",
            lambda: client.get_real_time_timetable(ENTITY, STOP),
        ),
        "get_disruptions": (
            "disruptions",
            lambda: client.get_disruptions(ENTITY, STOP),
        ),
        "get_transport_regions": (
            "transport_regions",
            lambda: client.get_transport_regions(),
        ),
        "get_transport_region": (
            "transport_region",
            lambda: client.get_transport_region(REGION),
        ),
    }
