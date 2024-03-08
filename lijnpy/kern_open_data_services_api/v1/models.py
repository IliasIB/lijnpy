from __future__ import annotations

from datetime import date

from pydantic import BaseModel, Field


class Direction(BaseModel):
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


class Disruption(BaseModel):
    """Represents a detour of a line

    Attributes:
        description (str): The description of the detour
        line_directions (list[Richting]): The directions of the line
    """

    description: str = Field(validation_alias="omschrijving")
    line_directions: list[Direction] = Field(validation_alias="lijnrichtingen")


class RealTimePassage(BaseModel):
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


class Detour(BaseModel):
    """Represents a detour of a line

    Attributes:
        title (str): The title of the detour
        description (str): The description of the detour
        period (OmleidingPeriode): The period of the detour
        detour_reference (int): The reference ID of the detour
        type (str): The type of the detour
        detour_days (list[str]): The days of the week when the detour is active
    """

    title: str = Field(validation_alias="titel")
    description: str = Field(validation_alias="omschrijving")
    period: DetourPeriod = Field(validation_alias="periode")
    # TODO: Add haltes en richtingen
    detour_reference: int = Field(validation_alias="referentieOmleiding")
    type: str
    detour_days: list[str] = Field(validation_alias="omleidingsDagen")


class PassageNote(BaseModel):
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


class RideNote(BaseModel):
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


class Passage(BaseModel):
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


class Timetable(BaseModel):
    """Represents a schedule

    Attributes:
        passages (list[Passage]): The passages of the schedule
        passage_notes (list[PassageNote]): The notes of the passages
        ride_notes (list[RideNote]): The notes of the rides
    """

    passages: list[Passage] = Field(validation_alias="doorkomsten")
    passage_notes: list[PassageNote] = Field(validation_alias="doorkomstNotas")
    ride_notes: list[RideNote] = Field(validation_alias="ritNotas")


class GeoCoordinate(BaseModel):
    """Represents a geographical coordinate

    Attributes:
        latitude (float): The latitude of the coordinate
        longitude (float): The longitude of the coordinate
    """

    latitude: float
    longitude: float


class StopInVicinity(BaseModel):
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


class TransportRegion(BaseModel):
    """Represents a transport region in Belgium

    Attributes:
        code (str): The code of the transport region
        name (str): The name of the transport region
        number (str): The number of the transport region
    """

    code: str
    name: str = Field(validation_alias="naam")
    number: int = Field(validation_alias="nr")


class RGB(BaseModel):
    """Represents a color

    Attributes:
        red (int): The red value of the color
        green (int): The green value of the color
        blue (int): The blue value of the color
    """

    red: int = Field(validation_alias="rood")
    green: int = Field(validation_alias="groen")
    blue: int = Field(validation_alias="blauw")


class Color(BaseModel):
    """Represents a color

    Attributes:
        code (str): The code of the color
        description (str): The description of the color
        rgb (RGB): The RGB values of the color
        hex (str): The hexadecimal value of the color
    """

    code: str
    description: str = Field(validation_alias="omschrijving")
    rgb: RGB
    hex: str


class Line(BaseModel):
    """Represents a line in Belgium

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


class Stop(BaseModel):
    """Represents a stop in Belgium

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
    language: str = Field(validation_alias="taal")
    municipality_number: int = Field(validation_alias="gemeentenummer")
    omschrijving_gemeente: str = Field(validation_alias="omschrijvingGemeente")
    geo_coordinate: GeoCoordinate = Field(validation_alias="geoCoordinaat")
    accessibilities: list[str] = Field(validation_alias="halteToegankelijkheden")
    is_main: bool | None = Field(default=None, validation_alias="hoofdHalte")


class Entity(BaseModel):
    """Represents an entity in Belgium

    Attributes:
        number (int): The number of the entity
        code (str): The code of the entity
        description (str): The description of the entity
    """

    number: int = Field(validation_alias="entiteitnummer")
    code: str = Field(validation_alias="entiteitcode")
    description: str = Field(validation_alias="omschrijving")


class Municipality(BaseModel):
    """Represents a municipality in Belgium

    Attributes:
        number (int): The number of the municipality
        description (str): The description of the municipality
        main_municipality (Municipality | None, optional): The main municipality of the municipality. Defaults to None.
    """

    number: int = Field(validation_alias="gemeentenummer")
    description: str = Field(validation_alias="omschrijving")
    main_municipality: Municipality | None = Field(
        default=None, validation_alias="hoofdGemeente"
    )
