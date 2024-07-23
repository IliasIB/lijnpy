from logging import Logger

from pydantic import TypeAdapter, ValidationError

from lijnpy._rest_adapter import DeLijnAPIException, RestAdapter
from lijnpy.models import (
    Detour,
    DetourList,
    Direction,
    DirectionList,
    Disruption,
    DisruptionList,
    Entity,
    EntityList,
    GeoCoordinate,
    Line,
    LineColor,
    LineColorList,
    LineList,
    Municipality,
    MunicipalityList,
    RealTimeTimetable,
    Stop,
    StopInVicinity,
    StopInVicinityList,
    StopList,
    Timetable,
    TransportRegion,
    TransportRegionList,
)


class KODSClientV1:
    def __init__(
        self,
        api_key: str = "",
        logger: Logger = Logger(__name__),
        http_client: RestAdapter | None = None,
    ):
        self.http_client = http_client or RestAdapter(
            "api.delijn.be/DLKernOpenData/api",
            api_key,
            "v1",
            True,
            logger,
        )
        self.logger = logger

    async def parse_api_call[T](self, path: str, cls: type[T]) -> T:
        """Parses result of API path and returns a model

        Args:
            path (str): The path to call on the API
            cls (type[T]): Class to validate the result of the API to

        Returns:
            T: A model validated from the result of the given path on the API
        """
        try:
            result = await self.http_client.get(path)
            assert result.data is not None
            type_adapter = TypeAdapter(cls)
            return type_adapter.validate_python(result.data)
        except (AssertionError, ValidationError) as e:
            self.logger.error(f"Failed to parse the response from the API: {e}")
            raise DeLijnAPIException from e

    async def get_colors(self) -> list[LineColor]:
        """Get a list of all colors

        Returns:
            list[LineColor]: A list of all colors
        """

        return (await self.parse_api_call("/kleuren", LineColorList)).colors

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
        return (await self.parse_api_call("/entiteiten", EntityList)).entities

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
        return (
            await self.parse_api_call(
                f"/entiteiten/{entity_number}/gemeenten", MunicipalityList
            )
        ).municipalities

    async def get_stops_by_entity(self, entity_number: int) -> list[Stop]:
        """Get a list of stops in Belgium for a given entity

        Args:
            entity_number (str): The number of the entity

        Returns:
            list[Stop]: A list of stops in Belgium for a given entity
        """

        return (
            await self.parse_api_call(f"/entiteiten/{entity_number}/haltes", StopList)
        ).stops

    async def get_lines_by_entity(self, entity_number: int) -> list[Line]:
        """Get a list of lines in Belgium for a given entity

        Args:
            entity_number (str): The number of the entity

        Returns:
            list[Line]: A list of lines in Belgium for a given entity
        """

        return (
            await self.parse_api_call(f"/entiteiten/{entity_number}/lijnen", LineList)
        ).lines

    async def get_municipalities(self) -> list[Municipality]:
        """Get a list of all municipalities in Belgium

        Returns:
            list[Municipality]: A list of all municipalities in Belgium
        """

        return (
            await self.parse_api_call("/gemeenten", MunicipalityList)
        ).municipalities

    async def get_stops(self, municipality_number: int) -> list[Stop]:
        """Get a list of stops in a municipality

        Args:
            municipality_number (int): The municipality number

        Returns:
            list[Stop]: A list of stops in the municipality
        """

        return (
            await self.parse_api_call(
                f"/gemeenten/{municipality_number}/haltes", StopList
            )
        ).stops

    async def get_lines(self, municipality_number: int) -> list[Line]:
        """Get a list of lines in a municipality

        Args:
            municipality_number (int): The municipality number

        Returns:
            list[Line]: A list of lines in the municipality
        """

        return (
            await self.parse_api_call(
                f"/gemeenten/{municipality_number}/lijnen", LineList
            )
        ).lines

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
    ) -> list[StopInVicinity]:
        """Get a list of all available stops in the neighbourhood of the given geo-coordinates

        Args:
            geo_coordinate (GeoCoordinate): The geo-coordinates to search around

        Returns:
            list[StopInVicinity]: A list of all available stops in the neighbourhood of the given geo-coordinates

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return (
            await self.parse_api_call(
                f"/haltes/indebuurt/{geo_coordinate.latitude},{geo_coordinate.longitude}",
                StopInVicinityList,
            )
        ).stops

    async def get_stop(self, entity_number: int, stop_number: int) -> Stop:
        """Get the stop with the given entity and stop number

        Args:
            entity_number (int): The number of the entity
            stop_number (int): The number of the stop

        Returns:
            Stop: The stop with the given entity and stop number

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/haltes/{entity_number}/{stop_number}",
            Stop,
        )

    async def get_timetable(self, entity_number: int, stop_number: int) -> Timetable:
        """Get the schedule of the stop with the given entity and stop number

        Returns:
            Timetable: The schedule of the stop with the given entity and stop number

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/haltes/{entity_number}/{stop_number}/dienstregelingen",
            Timetable,
        )

    async def get_directions(
        self, entity_number: int, stop_number: int
    ) -> list[Direction]:
        """Get the directions of the stop with the given entity and stop number

        Args:
            entity_number (int): The number of the entity
            stop_number (int): The number of the stop

        Returns:
            list[Direction]: The directions of the stop with the given entity and stop number

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return (
            await self.parse_api_call(
                f"/haltes/{entity_number}/{stop_number}/lijnrichtingen",
                DirectionList,
            )
        ).directions

    async def get_detours(self, entity_number: int, stop_number: int) -> list[Detour]:
        """Get the detours of the stop with the given entity and stop number

        Args:
            entity_number (int): The number of the entity
            stop_number (int): The number of the stop

        Returns:
            list[Detour]: The detours of the stop with the given entity and stop number

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return (
            await self.parse_api_call(
                f"/haltes/{entity_number}/{stop_number}/omleidingen",
                DetourList,
            )
        ).detours

    async def get_real_time_timetable(
        self, entity_number: int, stop_number: int
    ) -> RealTimeTimetable:
        """Get the real-time arrivals of the stop with the given entity and stop number

        Args:
            entity_number (int): The number of the entity
            stop_number (int): The number of the stop

        Returns:
            RealTimeTimetable: The real-time arrivals of the stop with the given entity and stop number

        Raises:
            DeLijnAPIException: If the API request fails
        """

        return await self.parse_api_call(
            f"/haltes/{entity_number}/{stop_number}/real-time-doorkomsten",
            RealTimeTimetable,
        )

    async def get_disruptions(
        self, entity_number: int, stop_number: int
    ) -> list[Disruption]:
        """Get the directions of the stop with the given entity and stop number

        Args:
            entity_number (int): The number of the entity
            stop_number (int): The number of the stop

        Returns:
            list[Disruption]: The disruptions of the stop with the given entity and stop number
        Raises:
            DeLijnAPIException: If the API request fails
        """

        return (
            await self.parse_api_call(
                f"/haltes/{entity_number}/{stop_number}/storingen",
                DisruptionList,
            )
        ).disruptions

    async def get_transport_regions(self) -> list[TransportRegion]:
        """Get a list of all transport regions

        Returns:
            list[TransportRegion]: A list of all transport regions
        """

        return (
            await self.parse_api_call(
                "/vervoerregios",
                TransportRegionList,
            )
        ).transport_regions

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

    async def get_lines_by_transport_region(
        self, transport_region_code: str
    ) -> list[Line]:
        """Get a list of lines by transport region code

        Args:
            transport_region_code (str): The code of the transport region

        Returns:
            list[Line]: A list of lines
        """

        return (
            await self.parse_api_call(
                f"/vervoerregios/{transport_region_code}/lijnen",
                LineList,
            )
        ).lines
