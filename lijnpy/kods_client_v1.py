from collections.abc import Mapping
from datetime import date, datetime
from logging import Logger, getLogger
from typing import Callable

from pydantic import TypeAdapter, ValidationError

from lijnpy._query import (
    format_bool,
    format_date,
    format_datetime,
    format_int,
)
from lijnpy._rest_adapter import DeLijnAPIException, RestAdapter
from lijnpy.enums import LineDirection
from lijnpy.models import (
    Detour,
    Direction,
    Disruption,
    Entity,
    GeoCoordinate,
    Line,
    LineColor,
    LineColorCodes,
    LineTimetable,
    Municipality,
    RealTimeLineTimetable,
    RealTimeTimetable,
    Stop,
    StopInVicinity,
    Timetable,
    TransportRegion,
)


class KODSClientV1:
    def __init__(
        self,
        api_key: str = "",
        logger: Logger | None = None,
        http_client: RestAdapter | None = None,
    ):
        self.logger = logger or getLogger(__name__)
        self.http_client = http_client or RestAdapter(
            "api.delijn.be/DLKernOpenData/api",
            api_key,
            "v1",
            True,
            self.logger,
        )

    async def close(self) -> None:
        """Close the HTTP session. Call this when you are done with the client,
        or use the client as an async context manager."""
        await self.http_client.close()

    async def __aenter__(self) -> "KODSClientV1":
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close()

    async def parse_api_call[T](
        self,
        path: str,
        cls: type[T],
        mapper: Callable[[dict], dict | list[dict]] | None = None,
        params: Mapping[str, str | None] | None = None,
    ) -> T:
        """Parses result of API path and returns a model

        Args:
            path (str): The path to call on the API
            cls (type[T]): Class to validate the result of the API to
            mapper (Callable[[dict], dict | list[dict]], optional): Mapper to extract
            value from the return value
            params (Mapping[str, str | None], optional): Query parameters, already
            formatted as strings. Parameters that are None are not sent.

        Returns:
            T: A model validated from the result of the given path on the API
        """
        query = {k: v for k, v in (params or {}).items() if v is not None}
        result = await self.http_client.get(path, query or None)
        if result.data is None:
            self.logger.error(f"The API returned no data for {path}")
            raise DeLijnAPIException(f"The API returned no data for {path}")
        try:
            data = result.data if mapper is None else mapper(result.data)
            return TypeAdapter(cls).validate_python(data)
        except ValidationError as e:
            first = e.errors()[0]
            self.logger.error(
                f"Failed to parse the response from {path}: {e.error_count()} "
                f"validation errors, first at {first['loc']}: {first['msg']}"
            )
            raise DeLijnAPIException from e
        except KeyError as e:
            self.logger.error(
                f"Failed to parse the response from {path}: missing key {e}"
            )
            raise DeLijnAPIException from e

    async def get_colors(self) -> list[LineColor]:
        """Get a list of all colors

        Returns:
            list[LineColor]: A list of all colors
        """

        return await self.parse_api_call(
            "/kleuren", list[LineColor], lambda x: x["kleuren"]
        )

    async def get_color(self, color_code: str) -> LineColor:
        """Get a color by its code

        Args:
            color_code (str): The code of the color

        Returns:
            LineColor: The color with the given code
        """

        return await self.parse_api_call(f"/kleuren/{color_code}", LineColor)

    async def get_entities(self) -> list[Entity]:
        """Get a list of all entities

        Returns:
            list[Entity]: A list of all entities
        """
        return await self.parse_api_call(
            "/entiteiten", list[Entity], lambda x: x["entiteiten"]
        )

    async def get_entity(self, entity_number: int) -> Entity:
        """Get an entity by its number

        Args:
            entity_number (int): The number of the entity

        Returns:
            Entity: The entity with the given number
        """
        return await self.parse_api_call(f"/entiteiten/{entity_number}", Entity)

    async def get_municipalities_by_entity(
        self, entity_number: int
    ) -> list[Municipality]:
        """Get a list of municipalities in Belgium for a given entity

        Args:
            entity_number (str): The number of the entity

        Returns:
            list[Municipality]: A list of municipalities in Belgium for a given entity
        """
        return await self.parse_api_call(
            f"/entiteiten/{entity_number}/gemeenten",
            list[Municipality],
            lambda x: x["gemeenten"],
        )

    async def get_stops_by_entity(
        self, entity_number: int, *, valid_on: datetime | date | None = None
    ) -> list[Stop]:
        """Get a list of stops in Belgium for a given entity

        Args:
            entity_number (int): The number of the entity
            valid_on (datetime | date, optional): Only return data valid at this
                moment, in local Belgian time without a time zone. A date means
                midnight. Defaults to now (decided by the API).

        Returns:
            list[Stop]: A list of stops in Belgium for a given entity
        """

        return await self.parse_api_call(
            f"/entiteiten/{entity_number}/haltes",
            list[Stop],
            lambda x: x["haltes"],
            {"geldigOp": format_datetime(valid_on)},
        )

    async def get_lines_by_entity(
        self, entity_number: int, *, valid_on: datetime | date | None = None
    ) -> list[Line]:
        """Get a list of lines in Belgium for a given entity

        Args:
            entity_number (int): The number of the entity
            valid_on (datetime | date, optional): Only return data valid at this
                moment, in local Belgian time without a time zone. A date means
                midnight. Defaults to now (decided by the API).

        Returns:
            list[Line]: A list of lines in Belgium for a given entity
        """

        return await self.parse_api_call(
            f"/entiteiten/{entity_number}/lijnen",
            list[Line],
            lambda x: x["lijnen"],
            {"geldigOp": format_datetime(valid_on)},
        )

    async def get_municipalities(self) -> list[Municipality]:
        """Get a list of all municipalities in Belgium

        Returns:
            list[Municipality]: A list of all municipalities in Belgium
        """

        return await self.parse_api_call(
            "/gemeenten", list[Municipality], lambda x: x["gemeenten"]
        )

    async def get_stops(
        self, municipality_number: int, *, valid_on: datetime | date | None = None
    ) -> list[Stop]:
        """Get a list of stops in a municipality

        Args:
            municipality_number (int): The municipality number
            valid_on (datetime | date, optional): Only return data valid at this
                moment, in local Belgian time without a time zone. A date means
                midnight. Defaults to now (decided by the API).

        Returns:
            list[Stop]: A list of stops in the municipality
        """

        return await self.parse_api_call(
            f"/gemeenten/{municipality_number}/haltes",
            list[Stop],
            lambda x: x["haltes"],
            {"geldigOp": format_datetime(valid_on)},
        )

    async def get_lines(
        self, municipality_number: int, *, valid_on: datetime | date | None = None
    ) -> list[Line]:
        """Get a list of lines in a municipality

        Args:
            municipality_number (int): The municipality number
            valid_on (datetime | date, optional): Only return data valid at this
                moment, in local Belgian time without a time zone. A date means
                midnight. Defaults to now (decided by the API).

        Returns:
            list[Line]: A list of lines in the municipality
        """

        return await self.parse_api_call(
            f"/gemeenten/{municipality_number}/lijnen",
            list[Line],
            lambda x: x["lijnen"],
            {"geldigOp": format_datetime(valid_on)},
        )

    async def get_all_lines(
        self, *, valid_on: datetime | date | None = None
    ) -> list[Line]:
        """Get a list of all lines in Belgium

        Args:
            valid_on (datetime | date, optional): Only return data valid at this
                moment, in local Belgian time without a time zone. A date means
                midnight. Defaults to now (decided by the API).

        Returns:
            list[Line]: A list of all lines

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            "/lijnen",
            list[Line],
            lambda x: x["lijnen"],
            {"geldigOp": format_datetime(valid_on)},
        )

    async def get_line(
        self,
        entity_number: int,
        line_number: int,
        *,
        valid_on: datetime | date | None = None,
    ) -> Line:
        """Get the line with the given entity and line number

        Args:
            entity_number (int): The number of the entity
            line_number (int): The number of the line
            valid_on (datetime | date, optional): Only return data valid at this
                moment, in local Belgian time without a time zone. A date means
                midnight. Defaults to now (decided by the API).

        Returns:
            Line: The line with the given entity and line number

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/lijnen/{entity_number}/{line_number}",
            Line,
            params={"geldigOp": format_datetime(valid_on)},
        )

    async def get_municipalities_by_line(
        self,
        entity_number: int,
        line_number: int,
        *,
        valid_on: datetime | date | None = None,
    ) -> list[Municipality]:
        """Get the municipalities a line passes through

        Args:
            entity_number (int): The number of the entity
            line_number (int): The number of the line
            valid_on (datetime | date, optional): Only return data valid at this
                moment, in local Belgian time without a time zone. A date means
                midnight. Defaults to now (decided by the API).

        Returns:
            list[Municipality]: The municipalities the line passes through

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/lijnen/{entity_number}/{line_number}/gemeenten",
            list[Municipality],
            lambda x: x["gemeenten"],
            {"geldigOp": format_datetime(valid_on)},
        )

    async def get_line_colors(
        self,
        entity_number: int,
        line_number: int,
        *,
        valid_on: datetime | date | None = None,
    ) -> LineColorCodes:
        """Get the color codes of a line

        Args:
            entity_number (int): The number of the entity
            line_number (int): The number of the line
            valid_on (datetime | date, optional): Only return data valid at this
                moment, in local Belgian time without a time zone. A date means
                midnight. Defaults to now (decided by the API).

        Returns:
            LineColorCodes: The color codes of the line; use `get_color` to look
                up a code

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/lijnen/{entity_number}/{line_number}/lijnkleuren",
            LineColorCodes,
            params={"geldigOp": format_datetime(valid_on)},
        )

    async def get_line_directions(
        self,
        entity_number: int,
        line_number: int,
        *,
        valid_on: datetime | date | None = None,
    ) -> list[Direction]:
        """Get the directions of a line

        Args:
            entity_number (int): The number of the entity
            line_number (int): The number of the line
            valid_on (datetime | date, optional): Only return data valid at this
                moment, in local Belgian time without a time zone. A date means
                midnight. Defaults to now (decided by the API).

        Returns:
            list[Direction]: The directions of the line. Most lines have two, some
                only run in one direction.

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/lijnen/{entity_number}/{line_number}/lijnrichtingen",
            list[Direction],
            lambda x: x["lijnrichtingen"],
            {"geldigOp": format_datetime(valid_on)},
        )

    async def get_line_direction(
        self,
        entity_number: int,
        line_number: int,
        direction: LineDirection,
        *,
        valid_on: datetime | date | None = None,
    ) -> Direction:
        """Get one direction of a line

        Args:
            entity_number (int): The number of the entity
            line_number (int): The number of the line
            direction (LineDirection): The direction of the line
            valid_on (datetime | date, optional): Only return data valid at this
                moment, in local Belgian time without a time zone. A date means
                midnight. Defaults to now (decided by the API).

        Returns:
            Direction: The direction of the line

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/lijnen/{entity_number}/{line_number}/lijnrichtingen/{direction.value}",
            Direction,
            params={"geldigOp": format_datetime(valid_on)},
        )

    async def get_line_direction_timetable(
        self,
        entity_number: int,
        line_number: int,
        direction: LineDirection,
        *,
        day: date | None = None,
    ) -> LineTimetable:
        """Get the schedule of a line direction, per ride

        Args:
            entity_number (int): The number of the entity
            line_number (int): The number of the line
            direction (LineDirection): The direction of the line
            day (date, optional): The day to get the data for. Defaults to today
                (decided by the API).

        Returns:
            LineTimetable: The rides of the line direction with their passages

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/lijnen/{entity_number}/{line_number}/lijnrichtingen/{direction.value}/dienstregelingen",
            LineTimetable,
            params={"datum": format_date(day)},
        )

    async def get_line_direction_ride(
        self,
        entity_number: int,
        line_number: int,
        direction: LineDirection,
        ride_number: int,
        *,
        day: date | None = None,
    ) -> LineTimetable:
        """Get a single ride of a line direction

        Args:
            entity_number (int): The number of the entity
            line_number (int): The number of the line
            direction (LineDirection): The direction of the line
            ride_number (int): The number of the ride
            day (date, optional): The day of the ride. Pass it: the API answered
                404 without it for the rides tried, even for rides that run today.

        Returns:
            LineTimetable: The ride, in `rides`, with its passages

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/lijnen/{entity_number}/{line_number}/lijnrichtingen/{direction.value}/rit/{ride_number}",
            LineTimetable,
            params={"datum": format_date(day)},
        )

    async def get_line_direction_stops(
        self,
        entity_number: int,
        line_number: int,
        direction: LineDirection,
        *,
        valid_on: datetime | date | None = None,
    ) -> list[Stop]:
        """Get the stops of a line direction

        Args:
            entity_number (int): The number of the entity
            line_number (int): The number of the line
            direction (LineDirection): The direction of the line
            valid_on (datetime | date, optional): Only return data valid at this
                moment, in local Belgian time without a time zone. A date means
                midnight. Defaults to now (decided by the API).

        Returns:
            list[Stop]: The stops of the line direction

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/lijnen/{entity_number}/{line_number}/lijnrichtingen/{direction.value}/haltes",
            list[Stop],
            lambda x: x["haltes"],
            {"geldigOp": format_datetime(valid_on)},
        )

    async def get_line_direction_detours(
        self,
        entity_number: int,
        line_number: int,
        direction: LineDirection,
        *,
        day: date | None = None,
    ) -> list[Detour]:
        """Get the detours of a line direction

        Args:
            entity_number (int): The number of the entity
            line_number (int): The number of the line
            direction (LineDirection): The direction of the line
            day (date, optional): The day to get the data for. Defaults to today
                (decided by the API).

        Returns:
            list[Detour]: The detours of the line direction

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/lijnen/{entity_number}/{line_number}/lijnrichtingen/{direction.value}/omleidingen",
            list[Detour],
            lambda x: x["omleidingen"],
            {"datum": format_date(day)},
        )

    async def get_line_direction_real_time_timetable(
        self,
        entity_number: int,
        line_number: int,
        direction: LineDirection,
    ) -> RealTimeLineTimetable:
        """Get the real-time schedule of a line direction, per ride

        Args:
            entity_number (int): The number of the entity
            line_number (int): The number of the line
            direction (LineDirection): The direction of the line

        Returns:
            RealTimeLineTimetable: The rides of the line direction with their
                real-time passages

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/lijnen/{entity_number}/{line_number}/lijnrichtingen/{direction.value}/real-time",
            RealTimeLineTimetable,
        )

    async def get_line_direction_disruptions(
        self,
        entity_number: int,
        line_number: int,
        direction: LineDirection,
        *,
        day: date | None = None,
    ) -> list[Disruption]:
        """Get the disruptions of a line direction

        Args:
            entity_number (int): The number of the entity
            line_number (int): The number of the line
            direction (LineDirection): The direction of the line
            day (date, optional): The day to get the data for. Defaults to today
                (decided by the API).

        Returns:
            list[Disruption]: The disruptions of the line direction

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/lijnen/{entity_number}/{line_number}/lijnrichtingen/{direction.value}/storingen",
            list[Disruption],
            lambda x: x["storingen"],
            {"datum": format_date(day)},
        )

    async def get_municipality(self, municipality_number: int) -> Municipality:
        """Get a municipality by its number

        Args:
            municipality_number (int): The number of the municipality

        Returns:
            Municipality: The municipality with the given number
        """

        return await self.parse_api_call(
            f"/gemeenten/{municipality_number}", Municipality
        )

    async def get_stops_in_vicinity(
        self,
        geo_coordinate: GeoCoordinate,
        *,
        radius: int | None = None,
        max_stops: int | None = None,
    ) -> list[StopInVicinity]:
        """Get a list of all available stops in the neighbourhood of the given geo-coordinates

        Args:
            geo_coordinate (GeoCoordinate): The geo-coordinates to search around
            radius (int, optional): The search radius in meters. Defaults to 750
                (decided by the API).
            max_stops (int, optional): The maximum number of stops to return, at
                most 50. Defaults to 50 (decided by the API, which answers a larger
                value with a 400 error).

        Returns:
            list[StopInVicinity]: A list of all available stops in the neighbourhood of the given geo-coordinates

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/haltes/indebuurt/{geo_coordinate.latitude},{geo_coordinate.longitude}",
            list[StopInVicinity],
            lambda x: x["haltes"],
            {
                "radius": format_int(radius),
                "maxAantalHaltes": format_int(max_stops),
            },
        )

    async def get_stop(
        self,
        entity_number: int,
        stop_number: int,
        *,
        valid_on: datetime | date | None = None,
    ) -> Stop:
        """Get the stop with the given entity and stop number

        Args:
            entity_number (int): The number of the entity
            stop_number (int): The number of the stop
            valid_on (datetime | date, optional): Only return data valid at this
                moment, in local Belgian time without a time zone. A date means
                midnight. Defaults to now (decided by the API).

        Returns:
            Stop: The stop with the given entity and stop number

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/haltes/{entity_number}/{stop_number}",
            Stop,
            params={"geldigOp": format_datetime(valid_on)},
        )

    async def get_timetable(
        self,
        entity_number: int,
        stop_number: int,
        *,
        day: date | None = None,
        include_last_passage: bool | None = None,
    ) -> Timetable:
        """Get the schedule of the stop with the given entity and stop number

        Args:
            entity_number (int): The number of the entity
            stop_number (int): The number of the stop
            day (date, optional): The day to get the data for. Defaults to today
                (decided by the API).
            include_last_passage (bool, optional): Whether to include the last
                passage of the previous day. Defaults to False (decided by the API).

        Returns:
            Timetable: The schedule of the stop with the given entity and stop number

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/haltes/{entity_number}/{stop_number}/dienstregelingen",
            Timetable,
            params={
                "datum": format_date(day),
                "inclusiefLaatsteDoorkomst": format_bool(include_last_passage),
            },
        )

    async def get_directions(
        self,
        entity_number: int,
        stop_number: int,
        *,
        valid_on: datetime | date | None = None,
    ) -> list[Direction]:
        """Get the directions of the stop with the given entity and stop number

        Args:
            entity_number (int): The number of the entity
            stop_number (int): The number of the stop
            valid_on (datetime | date, optional): Only return data valid at this
                moment, in local Belgian time without a time zone. A date means
                midnight. Defaults to now (decided by the API).

        Returns:
            list[Direction]: The directions of the stop with the given entity and stop number

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/haltes/{entity_number}/{stop_number}/lijnrichtingen",
            list[Direction],
            lambda x: x["lijnrichtingen"],
            {"geldigOp": format_datetime(valid_on)},
        )

    async def get_detours(
        self, entity_number: int, stop_number: int, *, day: date | None = None
    ) -> list[Detour]:
        """Get the detours of the stop with the given entity and stop number

        Args:
            entity_number (int): The number of the entity
            stop_number (int): The number of the stop
            day (date, optional): The day to get the data for. Defaults to today
                (decided by the API).

        Returns:
            list[Detour]: The detours of the stop with the given entity and stop number

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/haltes/{entity_number}/{stop_number}/omleidingen",
            list[Detour],
            lambda x: x["omleidingen"],
            {"datum": format_date(day)},
        )

    async def get_real_time_timetable(
        self,
        entity_number: int,
        stop_number: int,
        *,
        max_passages: int | None = None,
    ) -> RealTimeTimetable:
        """Get the real-time arrivals of the stop with the given entity and stop number

        Args:
            entity_number (int): The number of the entity
            stop_number (int): The number of the stop
            max_passages (int, optional): The maximum number of passages to return.
                Defaults to 10 (decided by the API).

        Returns:
            RealTimeTimetable: The real-time arrivals of the stop with the given entity and stop number

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/haltes/{entity_number}/{stop_number}/real-time",
            RealTimeTimetable,
            params={"maxAantalDoorkomsten": format_int(max_passages)},
        )

    async def get_disruptions(
        self, entity_number: int, stop_number: int, *, day: date | None = None
    ) -> list[Disruption]:
        """Get the disruptions of the stop with the given entity and stop number

        Args:
            entity_number (int): The number of the entity
            stop_number (int): The number of the stop
            day (date, optional): The day to get the data for. Defaults to today
                (decided by the API).

        Returns:
            list[Disruption]: The disruptions of the stop with the given entity and stop number

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/haltes/{entity_number}/{stop_number}/storingen",
            list[Disruption],
            lambda x: x["storingen"],
            {"datum": format_date(day)},
        )

    async def get_transport_regions(self) -> list[TransportRegion]:
        """Get a list of all transport regions

        Returns:
            list[TransportRegion]: A list of all transport regions
        """

        return await self.parse_api_call(
            "/vervoerregios", list[TransportRegion], lambda x: x["vervoerRegios"]
        )

    async def get_transport_region(self, transport_region_code: str) -> TransportRegion:
        """Get a transport region by code

        Args:
            transport_region_code (str): The code of the transport region

        Returns:
            TransportRegion: The transport region
        """

        return await self.parse_api_call(
            f"/vervoerregios/{transport_region_code}",
            TransportRegion,
        )
