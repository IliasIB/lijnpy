from pydantic import BaseModel, Field

from lijnpy.kods.api.v1.models.utils import DetourPeriod, GeoCoordinate, Link


class StopResponse(BaseModel):
    """Represents a response from the stop API

    Attributes:
        entity_number (int): The number of the entity
        number (int): The number of the stop
        description (str): The description of the stop
        description_long (str): The long description of the stop
        language (str): The language of the stop
        municipality_number (int): The number of the municipality
        omschrijving_gemeente (str): The description of the municipality
        geo_coordinate (GeoCoordinate): The geographical coordinate of the stop
        accessibilities (list[str]): The accessibilities of the stop
        is_main (bool): Whether the stop is main
    """

    entity_number: int = Field(validation_alias="entiteitnummer")
    number: int = Field(validation_alias="haltenummer")
    description: str = Field(validation_alias="omschrijving")
    description_long: str = Field(validation_alias="omschrijvingLang")
    municipality_number: int = Field(validation_alias="gemeentenummer")
    omschrijving_gemeente: str = Field(validation_alias="omschrijvingGemeente")
    geo_coordinate: GeoCoordinate = Field(validation_alias="geoCoordinaat")
    accessibilities: list[str] = Field(validation_alias="halteToegankelijkheden")
    is_main: bool | None = Field(default=None, validation_alias="hoofdHalte")
    language: str = Field(validation_alias="taal")
    links: list[Link] = Field(validation_alias="links")


class StopsResponse(BaseModel):
    """Represents a response from the stops API

    Attributes:
        stops (list[Stop]): The stops of the response
    """

    class Stop(BaseModel):
        entity_number: int = Field(validation_alias="entiteitnummer")
        number: int = Field(validation_alias="haltenummer")
        description: str = Field(validation_alias="omschrijving")
        description_long: str = Field(validation_alias="omschrijvingLang")
        municipality_number: int = Field(validation_alias="gemeentenummer")
        omschrijving_gemeente: str = Field(validation_alias="omschrijvingGemeente")
        geo_coordinate: GeoCoordinate = Field(validation_alias="geoCoordinaat")
        accessibilities: list[str] = Field(validation_alias="halteToegankelijkheden")
        is_main: bool | None = Field(default=None, validation_alias="hoofdHalte")
        language: str = Field(validation_alias="taal")
        links: list[Link] = Field(validation_alias="links")

    stops: list[Stop] = Field(validation_alias="haltes")
    links: list[Link] = Field(validation_alias="links")


class StopsInVicinityResponse(BaseModel):
    """Represents a response from the stops in vicinity API

    Attributes:
        stops (list[StopInVicinity]): The stops in the neighborhood of the geo-coordinate
    """

    class StopInVicinity(BaseModel):
        type: str
        id: int
        name: str = Field(validation_alias="naam")
        distance: int = Field(validation_alias="afstand")
        geo_coordinate: GeoCoordinate = Field(validation_alias="geoCoordinaat")
        links: list[Link] = Field(validation_alias="links")

    stops: list[StopInVicinity] = Field(validation_alias="haltes")
    links: list[Link] = Field(validation_alias="links")


class TimetableResponse(BaseModel):
    """Represents a schedule

    Attributes:
        passages (list[Passage]): The passages of the schedule
        passage_notes (list[PassageNote]): The notes of the passages
        ride_notes (list[RideNote]): The notes of the rides
    """

    class StopPassages(BaseModel):
        class Passage(BaseModel):
            entity_number: int = Field(validation_alias="entiteitnummer")
            line_number: int = Field(validation_alias="lijnnummer")
            direction: str = Field(validation_alias="richting")
            ride_number: int = Field(validation_alias="ritnummer")
            destination: str = Field(validation_alias="bestemming")
            destination_place: str = Field(validation_alias="plaatsBestemming")
            vias: list[str] | None = None
            # TODO: Properly parse the datetime
            timetable_timestamp: str = Field(validation_alias="dienstregelingTijdstip")
            links: list[Link] = Field(validation_alias="links")

        stop_number: int = Field(validation_alias="haltenummer")
        passages: list[Passage] = Field(validation_alias="doorkomsten")

    class RideNote(BaseModel):
        id: int
        title: str = Field(validation_alias="titel")
        ride_number: int = Field(validation_alias="ritnummer")
        stop_number: int = Field(validation_alias="haltenummer")
        description: str = Field(validation_alias="omschrijving")
        entity_number: int = Field(validation_alias="entiteitnummer")
        line_number: int = Field(validation_alias="lijnnummer")
        direction: str = Field(validation_alias="richting")
        links: list[Link] = Field(validation_alias="links")

    class PassageNote(BaseModel):
        id: int
        title: str = Field(validation_alias="titel")
        ride_number: int = Field(validation_alias="ritnummer")
        stop_number: int = Field(validation_alias="haltenummer")
        description: str = Field(validation_alias="omschrijving")
        entity_number: int = Field(validation_alias="entiteitnummer")
        line_number: int = Field(validation_alias="lijnnummer")
        direction: str = Field(validation_alias="richting")
        links: list[Link] = Field(validation_alias="links")

    class Detour(BaseModel):
        class Direction(BaseModel):
            entity_number: int = Field(validation_alias="entiteitnummer")
            line_number: int = Field(validation_alias="lijnnummer")
            direction: str = Field(validation_alias="richting")
            description: str = Field(validation_alias="omschrijving")
            links: list[Link] = Field(validation_alias="links")

        title: str = Field(validation_alias="titel")
        description: str = Field(validation_alias="omschrijving")
        period: DetourPeriod = Field(validation_alias="periode")
        directions: list[Direction] = Field(validation_alias="lijnrichtingen")
        detour_reference: int = Field(validation_alias="referentieOmleiding")
        detour_days: list[str] = Field(validation_alias="omleidingsDagen")
        links: list[Link] = Field(validation_alias="links")

    passages: list[StopPassages] = Field(validation_alias="halteDoorkomsten")
    passage_notes: list[PassageNote] = Field(validation_alias="doorkomstNotas")
    ride_notes: list[RideNote] = Field(validation_alias="ritNotas")
    detours: list[Detour] = Field(validation_alias="omleidingen")
    links: list[Link] = Field(validation_alias="links")


class DirectionsResponse(BaseModel):
    """Represents the directions of a stop

    Attributes:
        directions (list[Direction]): The directions of the stop
    """

    class Direction(BaseModel):
        entity_number: int = Field(validation_alias="entiteitnummer")
        line_number: int = Field(validation_alias="lijnnummer")
        direction: str = Field(validation_alias="richting")
        description: str = Field(validation_alias="omschrijving")
        links: list[Link] = Field(validation_alias="links")

    directions: list[Direction] = Field(validation_alias="lijnrichtingen")
    links: list[Link] = Field(validation_alias="links")


class DetoursResponse(BaseModel):
    """Represents the detours of a stop

    Attributes:
        detours (list[Detour]): The detours of the stop
    """

    class Detour(BaseModel):
        class Direction(BaseModel):
            entity_number: int = Field(validation_alias="entiteitnummer")
            line_number: int = Field(validation_alias="lijnnummer")
            direction: str = Field(validation_alias="richting")
            description: str = Field(validation_alias="omschrijving")
            links: list[Link] = Field(validation_alias="links")

        title: str = Field(validation_alias="titel")
        description: str = Field(validation_alias="omschrijving")
        period: DetourPeriod = Field(validation_alias="periode")
        directions: list[Direction] = Field(validation_alias="lijnrichtingen")
        detour_reference: int = Field(validation_alias="referentieOmleiding")
        detour_days: list[str] = Field(validation_alias="omleidingsDagen")
        links: list[Link] = Field(validation_alias="links")

    detours: list[Detour] = Field(validation_alias="omleidingen")
    links: list[Link] = Field(validation_alias="links")


class RealTimePassagesResponse(BaseModel):
    """Represents the real-time arrivals of a stop

    Attributes:
        passages (list[RealTimePassageStopResponse]): The real-time arrivals of the stop
        passage_notes (list[PassageNoteResponse]): The notes of the passages
        ride_notes (list[RideNoteResponse]): The notes of the rides
        detours (list[DetourResponse]): The detours of the stop
    """

    class StopPassages(BaseModel):
        class Passage(BaseModel):
            entity_number: int = Field(validation_alias="entiteitnummer")
            line_number: int = Field(validation_alias="lijnnummer")
            direction: str = Field(validation_alias="richting")
            ride_number: int = Field(validation_alias="ritnummer")
            destination: str = Field(validation_alias="bestemming")
            vias: list[str] | None = Field(default=None)
            timetable_timestamp: str = Field(validation_alias="dienstregelingTijdstip")
            real_time_timestamp: str = Field(validation_alias="real-timeTijdstip")
            vrtnum: int
            prediction_statuses: list[str] = Field(
                validation_alias="predictionStatussen"
            )

        stop_number: int = Field(validation_alias="haltenummer")
        passages: list[Passage] = Field(validation_alias="doorkomsten")

    class RideNote(BaseModel):
        id: int
        title: str = Field(validation_alias="titel")
        ride_number: int = Field(validation_alias="ritnummer")
        stop_number: int = Field(validation_alias="haltenummer")
        description: str = Field(validation_alias="omschrijving")
        entity_number: int = Field(validation_alias="entiteitnummer")
        line_number: int = Field(validation_alias="lijnnummer")
        direction: str = Field(validation_alias="richting")
        links: list[Link] = Field(validation_alias="links")

    class PassageNote(BaseModel):
        id: int
        title: str = Field(validation_alias="titel")
        ride_number: int = Field(validation_alias="ritnummer")
        stop_number: int = Field(validation_alias="haltenummer")
        description: str = Field(validation_alias="omschrijving")
        entity_number: int = Field(validation_alias="entiteitnummer")
        line_number: int = Field(validation_alias="lijnnummer")
        direction: str = Field(validation_alias="richting")
        links: list[Link] = Field(validation_alias="links")

    class Detour(BaseModel):
        class Direction(BaseModel):
            entity_number: int = Field(validation_alias="entiteitnummer")
            line_number: int = Field(validation_alias="lijnnummer")
            direction: str = Field(validation_alias="richting")
            description: str = Field(validation_alias="omschrijving")
            links: list[Link] = Field(validation_alias="links")

    passages: list[StopPassages] = Field(validation_alias="halteDoorkomsten")
    passage_notes: list[PassageNote] = Field(validation_alias="doorkomstNotas")
    ride_notes: list[RideNote] = Field(validation_alias="ritNotas")
    detours: list[Detour] = Field(validation_alias="omleidingen")
    links: list[Link] = Field(validation_alias="links")


class DisruptionsResponse(BaseModel):
    """Represents the disruptions of a stop

    Attributes:
        disruptions (list[Disruption]): The disruptions of the stop
    """

    class Disruption(BaseModel):
        class Direction(BaseModel):
            entity_number: int = Field(validation_alias="entiteitnummer")
            line_number: int = Field(validation_alias="lijnnummer")
            direction: str = Field(validation_alias="richting")
            description: str = Field(validation_alias="omschrijving")
            links: list[Link] = Field(validation_alias="links")

        description: str = Field(validation_alias="omschrijving")
        line_directions: list[Direction] = Field(validation_alias="lijnrichtingen")

    disruptions: list[Disruption] = Field(validation_alias="storingen")
    links: list[Link] = Field(validation_alias="links")
