from __future__ import annotations

from datetime import date

from pydantic import BaseModel, Field, HttpUrl


class Link(BaseModel):
    """Represents a link

    Attributes:
        relation (str): The relation of the link
        url (str): The URL of the link
    """

    relation: str = Field(validation_alias="rel")
    url: HttpUrl = Field(validation_alias="url")


class Response(BaseModel):
    """Represents a response from the API

    Attributes:
        links (list[Link]): The links of the response
    """

    links: list[Link] | None = None


class DirectionResponse(Response):
    """Represents a direction of a line

    Attributes:
        entity_number (int): The number of the entity
        line_number (int): The number of the line
        direction (str): The direction of the line
        description (str): The description of the direction
    """

    entity_number: int = Field(validation_alias="entiteitnummer")
    line_number: int = Field(validation_alias="lijnnummer")
    direction: str = Field(validation_alias="richting")
    description: str = Field(validation_alias="omschrijving")


class DirectionsResponse(Response):
    """Represents the directions of a stop

    Attributes:
        directions (list[Direction]): The directions of the stop
    """

    directions: list[DirectionResponse] = Field(validation_alias="lijnrichtingen")


class DisruptionResponse(BaseModel):
    """Represents a detour of a line

    Attributes:
        description (str): The description of the detour
        line_directions (list[Richting]): The directions of the line
    """

    description: str = Field(validation_alias="omschrijving")
    line_directions: list[DirectionResponse] = Field(validation_alias="lijnrichtingen")


class DisruptionsResponse(Response):
    """Represents the disruptions of a stop

    Attributes:
        disruptions (list[Disruption]): The disruptions of the stop
    """

    disruptions: list[DisruptionResponse] = Field(validation_alias="storingen")


class RealTimePassageResponse(Response):
    """Represents a real-time passage of a vehicle at a stop

    Attributes:
        entity_number (int): The number of the entity
        line_number (int): The number of the line
        direction (str): The direction of the line
        ride_number (int): The number of the ride
        destination (str): The destination of the ride
        vias (list[str], optional): The vias of the ride. Defaults to None.
        timetable_timestamp (str): The schedule time of the ride
        real_time_timestamp (str): The real-time time of the ride
        vrtnum (int): The number of the ride
        prediction_statuses (list[str]): The prediction statuses of the ride
    """

    entity_number: int = Field(validation_alias="entiteitnummer")
    line_number: int = Field(validation_alias="lijnnummer")
    direction: str = Field(validation_alias="richting")
    ride_number: int = Field(validation_alias="ritnummer")
    destination: str = Field(validation_alias="bestemming")
    vias: list[str] | None = Field(default=None)
    timetable_timestamp: str = Field(validation_alias="dienstregelingTijdstip")
    real_time_timestamp: str = Field(validation_alias="real-timeTijdstip")
    vrtnum: int
    prediction_statuses: list[str] = Field(validation_alias="predictionStatussen")


class DetourPeriod(BaseModel):
    """Represents a period of a detour of a line

    Attributes:
        start_date (str): The start date of the period
        end_date (str, optional): The end date of the period. Defaults to None.
    """

    start_date: str = Field(validation_alias="startDatum")
    end_date: str | None = Field(default=None, validation_alias="eindDatum")


class DetourResponse(Response):
    """Represents a detour of a line

    Attributes:
        title (str): The title of the detour
        description (str): The description of the detour
        period (DetourPeriod): The period of the detour
        directions (list[DirectionResponse]): The directions of the line
        detour_reference (int): The reference ID of the detour
        detour_days (list[str]): The days of the week when the detour is active
    """

    title: str = Field(validation_alias="titel")
    description: str = Field(validation_alias="omschrijving")
    period: DetourPeriod = Field(validation_alias="periode")
    directions: list[DirectionResponse] = Field(validation_alias="lijnrichtingen")
    detour_reference: int = Field(validation_alias="referentieOmleiding")
    detour_days: list[str] = Field(validation_alias="omleidingsDagen")


class DetoursResponse(Response):
    """Represents the detours of a stop

    Attributes:
        detours (list[Detour]): The detours of the stop
    """

    detours: list[DetourResponse] = Field(validation_alias="omleidingen")


class PassageNoteResponse(Response):
    """Represents a note of a passage of a vehicle at a stop

    Attributes:
        id (int): The ID of the note
        title (str): The title of the note
        ride_number (int): The number of the ride
        stop_number (int): The number of the stop
        description (str): The description of the note
        entity_number (int): The number of the entity
        line_number (int): The number of the line
        direction (str): The direction of the line
    """

    id: int
    title: str = Field(validation_alias="titel")
    ride_number: int = Field(validation_alias="ritnummer")
    stop_number: int = Field(validation_alias="haltenummer")
    description: str = Field(validation_alias="omschrijving")
    entity_number: int = Field(validation_alias="entiteitnummer")
    line_number: int = Field(validation_alias="lijnnummer")
    direction: str = Field(validation_alias="richting")


class PassageNotesResponse(BaseModel):
    """Represents the notes of a passage of a vehicle at a stop

    Attributes:
        notes (list[PassageNote]): The notes of the passage
    """

    notes: list[PassageNoteResponse] = Field(validation_alias="doorkomstNotas")


class RideNoteResponse(Response):
    """Represents a note of a ride

    Attributes:
        id (int): The ID of the note
        title (str): The title of the note
        ride_number (int): The number of the ride
        stop_number (int): The number of the stop
        description (str): The description of the note
        entity_number (int): The number of the entity
        line_number (int): The number of the line
        direction (str): The direction of the line
    """

    id: int
    title: str = Field(validation_alias="titel")
    ride_number: int = Field(validation_alias="ritnummer")
    stop_number: int = Field(validation_alias="haltenummer")
    description: str = Field(validation_alias="omschrijving")
    entity_number: int = Field(validation_alias="entiteitnummer")
    line_number: int = Field(validation_alias="lijnnummer")
    direction: str = Field(validation_alias="richting")


class RideNotesResponse(BaseModel):
    """Represents the notes of a ride

    Attributes:
        notes (list[RideNote]): The notes of the ride
    """

    notes: list[RideNoteResponse] = Field(validation_alias="ritNotas")


class PassageResponse(Response):
    """Represents a passage of a vehicle at a stop

    Attributes:
        entity_number (str): The number of the entity
        line_number (int): The number of the line
        direction (str): The direction of the line
        ride_number (int): The number of the ride
        destination (str): The destination of the ride
        destination_place (str): The place of the destination
        vias (str): The vias of the ride
        timetable_timestamp (str): The schedule time of the ride
    """

    entity_number: int = Field(validation_alias="entiteitnummer")
    line_number: int = Field(validation_alias="lijnnummer")
    direction: str = Field(validation_alias="richting")
    ride_number: int = Field(validation_alias="ritnummer")
    destination: str = Field(validation_alias="bestemming")
    destination_place: str = Field(validation_alias="plaatsBestemming")
    vias: list[str] | None = None
    # TODO: Properly parse the datetime
    timetable_timestamp: str = Field(validation_alias="dienstregelingTijdstip")


class StopPassages(BaseModel):
    """Represents the passages of a stop

    Attributes:
        passages (list[Passage]): The passages of the stop
    """

    stop_number: int = Field(validation_alias="haltenummer")
    passages: list[PassageResponse] = Field(validation_alias="doorkomsten")


class TimetableResponse(Response):
    """Represents a schedule

    Attributes:
        passages (list[Passage]): The passages of the schedule
        passage_notes (list[PassageNote]): The notes of the passages
        ride_notes (list[RideNote]): The notes of the rides
    """

    passages: list[StopPassages] = Field(validation_alias="halteDoorkomsten")
    passage_notes: list[PassageNoteResponse] = Field(validation_alias="doorkomstNotas")
    ride_notes: list[RideNoteResponse] = Field(validation_alias="ritNotas")
    detours: list[DetourResponse] = Field(validation_alias="omleidingen")


class RealTimePassageStopResponse(BaseModel):
    """Represents a list of real-time passages

    Attributes:
        stop_number (int): The number of the stop
        passages (list[RealTimePassage]): The real-time passages
    """

    stop_number: int = Field(validation_alias="haltenummer")
    passages: list[RealTimePassageResponse] = Field(validation_alias="doorkomsten")


class RealTimePassagesResponse(Response):
    """Represents the real-time arrivals of a stop

    Attributes:
        passages (list[RealTimePassageStopResponse]): The real-time arrivals of the stop
        passage_notes (list[PassageNoteResponse]): The notes of the passages
        ride_notes (list[RideNoteResponse]): The notes of the rides
        detours (list[DetourResponse]): The detours of the stop
    """

    passages: list[RealTimePassageStopResponse] = Field(
        validation_alias="halteDoorkomsten"
    )
    passage_notes: list[PassageNoteResponse] = Field(validation_alias="doorkomstNotas")
    ride_notes: list[RideNoteResponse] = Field(validation_alias="ritNotas")
    detours: list[DetourResponse] = Field(validation_alias="omleidingen")


class GeoCoordinate(BaseModel):
    """Represents a geographical coordinate

    Attributes:
        latitude (float): The latitude of the coordinate
        longitude (float): The longitude of the coordinate
    """

    latitude: float
    longitude: float


class StopsInVicinityResponse(Response):
    """Represents a response from the stops in vicinity API

    Attributes:
        stops (list[StopInVicinityResponse]): The stops in the neighborhood of the geo-coordinate
    """

    stops: list[StopInVicinityResponse] = Field(validation_alias="haltes")


class StopInVicinityResponse(Response):
    """Represents a stop in the neighborhood of a given geo-coordinate

    Attributes:
        type (str): The type of the stop
        id (str): The ID of the stop
        name (str): The name of the stop
        distance (int): The distance of the stop
        geo_coordinate (GeoCoordinate): The geographical coordinate of the stop
    """

    type: str
    id: int
    name: str = Field(validation_alias="naam")
    distance: int = Field(validation_alias="afstand")
    geo_coordinate: GeoCoordinate = Field(validation_alias="geoCoordinaat")


class TransportRegionResponse(Response):
    """Represents a transport region in Belgium

    Attributes:
        code (str): The code of the transport region
        name (str): The name of the transport region
        number (str): The number of the transport region
    """

    code: str
    name: str = Field(validation_alias="naam")
    number: int = Field(validation_alias="nr")


class TransportRegionsResponse(Response):
    """Represents a response from the transport regions API

    Attributes:
        transport_regions (list[TransportRegion]): The transport regions of the response
    """

    transport_regions: list[TransportRegionResponse] = Field(
        validation_alias="vervoerRegios"
    )


class RGBResponse(BaseModel):
    """Represents a color

    Attributes:
        red (int): The red value of the color
        green (int): The green value of the color
        blue (int): The blue value of the color
    """

    red: int = Field(validation_alias="rood")
    green: int = Field(validation_alias="groen")
    blue: int = Field(validation_alias="blauw")


class ColorsResponse(Response):
    """Represents a response from the colors API

    Attributes:
        colors (list[Color]): The colors of the response
    """

    colors: list[ColorResponse] = Field(validation_alias="kleuren")


class ColorResponse(Response):
    """Represents a response from the color API

    Attributes:
        code (str): The code of the color
        description (str): The description of the color
        rgb (RGB): The RGB values of the color
        hex (str): The hexadecimal value of the color
    """

    code: str
    description: str = Field(validation_alias="omschrijving")
    rgb: RGBResponse
    hex: str


class LinesResponse(Response):
    """Represents a response from the lines API

    Attributes:
        lines (list[Line]): The lines of the response
    """

    lines: list[LineResponse] = Field(validation_alias="lijnen")


class LineResponse(BaseModel):
    """Represents a response from the line API

    Attributes:
        entity_number (int): The number of the entity
        line_number (int): The number of the line
        line_number_public (str): The public number of the line
        description (str): The description of the line
        transport_region_code (str): The code of the transport region
        is_public (bool): Whether the line is public
        transport_type (str): The type of the transport
        operation_type (str): The type of the operation
        valid_from (str): The start date of the line
        valid_to (str): The end date of the line
    """

    entity_number: int = Field(validation_alias="entiteitnummer")
    line_number: int = Field(validation_alias="lijnnummer")
    line_number_public: str = Field(validation_alias="lijnnummerPubliek")
    description: str = Field(validation_alias="omschrijving")
    transport_region_code: str = Field(validation_alias="vervoerRegioCode")
    is_public: bool = Field(validation_alias="publiek")
    transport_type: str = Field(validation_alias="vervoertype")
    operation_type: str = Field(validation_alias="bedieningtype")
    valid_from: date = Field(validation_alias="lijnGeldigVan")
    valid_to: date = Field(validation_alias="lijnGeldigTot")


class StopsResponse(Response):
    """Represents a response from the stops API

    Attributes:
        stops (list[Stop]): The stops of the response
    """

    stops: list[StopResponse] = Field(validation_alias="haltes")


class StopResponse(Response):
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


class EntitiesResponse(Response):
    """Represents a response from the entities API

    Attributes:
        entities (list[Entity]): The entities of the response
    """

    entities: list[EntityResponse] = Field(validation_alias="entiteiten")


class EntityResponse(Response):
    """Represents a response from the entity API

    Attributes:
        number (int): The number of the entity
        code (str): The code of the entity
        description (str): The description of the entity
    """

    number: int = Field(validation_alias="entiteitnummer")
    code: str = Field(validation_alias="entiteitcode")
    description: str = Field(validation_alias="omschrijving")


class MunicipalitiesResponse(Response):
    """Represents a response from the municipalities API

    Attributes:
        municipalities (list[MunicipalityResponse]): The municipalities of the response
    """

    municipalities: list[MunicipalityResponse] = Field(validation_alias="gemeenten")


class MunicipalityResponse(Response):
    """Represents a response from the municipality API

    Attributes:
        number (int): The number of the municipality
        description (str): The description of the municipality
        main_municipality (Municipality | None, optional): The main municipality of the municipality. Defaults to None.
    """

    number: int = Field(validation_alias="gemeentenummer")
    description: str = Field(validation_alias="omschrijving")
    main_municipality: MunicipalityResponse | None = Field(
        default=None, validation_alias="hoofdGemeente"
    )
