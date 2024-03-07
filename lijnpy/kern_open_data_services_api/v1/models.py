from datetime import date

from pydantic import BaseModel, Field


class Richting(BaseModel):
    """Represents a direction of a line

    Attributes:
        entiteitnummer (str): The number of the entity
        lijnnummer (str): The number of the line
        richting (str): The direction of the line
        omschrijving (str): The description of the direction
        links (list[Link]): The links to other resources related to the direction
    """

    entiteitnummer: int
    lijnnummer: int
    richting: str
    omschrijving: str


class Storing(BaseModel):
    """Represents a detour of a line

    Attributes:
        omschrijving (str): The description of the detour
        lijnrichtingen (list[Richting]): The directions of the line
    """

    omschrijving: str
    lijnrichtingen: list[Richting]


class RealTimeDoorkomst(BaseModel):
    """Represents a real-time passage of a vehicle at a stop

    Attributes:
        entiteitnummer (str): The number of the entity
        lijnnummer (int): The number of the line
        richting (str): The direction of the line
        ritnummer (int): The number of the ride
        bestemming (str): The destination of the ride
        vias (list[str], optional): The vias of the ride. Defaults to None.
        dienstregeling_tijdstip (str): The schedule time of the ride
        real_time_tijdstip (str): The real-time time of the ride
        vrtnum (int): The number of the real-time passage
        prediction_statussen (list[str]): The status of the real-time passage
        links (list[Link]): The links to other resources related to the real-time passage
    """

    entiteitnummer: int
    lijnnummer: int
    richting: str
    # TODO: Search automatic pydantic conversion to int
    ritnummer: int
    bestemming: str
    vias: list[str] | None = Field(default=None)
    dienstregeling_tijdstip: str = Field(validation_alias="dienstregelingTijdstip")
    real_time_tijdstip: str = Field(validation_alias="real-timeTijdstip")
    vrtnum: int
    prediction_statussen: list[str] = Field(validation_alias="predictionStatussen")


class OmleidingPeriode(BaseModel):
    """Represents a period of a detour of a line

    Attributes:
        start_datum (str): The start date of the period
        eind_datum (str, optional): The end date of the period. Defaults to None.
    """

    start_datum: str = Field(validation_alias="startDatum")
    eind_datum: str | None = Field(default=None, validation_alias="eindDatum")


class Omleiding(BaseModel):
    """Represents a detour of a line

    Attributes:
        titel (str): The title of the detour
        omschrijving (str): The description of the detour
        periode (OmleidingPeriode): The period of the detour
        referentie_omleiding (int): The reference ID of the detour
        type (str): The type of the detour
        omleidings_dagen (list[str]): The days of the week when the detour is active
        links (list[Link]): The links to other resources related to the detour
    """

    titel: str
    omschrijving: str
    periode: OmleidingPeriode
    # TODO: Add haltes en richtingen
    referentie_omleiding: int = Field(validation_alias="referentieOmleiding")
    type: str
    omleidings_dagen: list[str] = Field(validation_alias="omleidingsDagen")


class DoorkomstNota(BaseModel):
    """Represents a note of a passage of a vehicle at a stop

    Attributes:
        id (int): The ID of the note
        titel (str): The title of the note
        ritnummer (int): The number of the ride
        haltenummer (int): The number of the stop
        omschrijving (str): The description of the note
        entiteitnummer (int): The number of the entity
        lijnnummer (int): The number of the line
        richting (str): The direction of the line
    """

    id: int
    titel: str
    ritnummer: int
    haltenummer: int
    omschrijving: str
    entiteitnummer: int
    lijnnummer: int
    richting: str


class RitNota(BaseModel):
    """Represents a note of a ride

    Attributes:
        id (int): The ID of the note
        titel (str): The title of the note
        ritnummer (int): The number of the ride
        haltenummer (int): The number of the stop
        omschrijving (str): The description of the note
        entiteitnummer (int): The number of the entity
        lijnnummer (int): The number of the line
        richting (str): The direction of the line
    """

    id: int
    titel: str
    # TODO: Convert to int
    ritnummer: int
    haltenummer: int
    omschrijving: str
    entiteitnummer: int
    lijnnummer: int
    richting: str


class Doorkomst(BaseModel):
    """Represents a passage of a vehicle at a stop

    Attributes:
        entiteitnummer (str): The number of the entity
        lijnnummer (int): The number of the line
        richting (str): The direction of the line
        ritnummer (int): The number of the ride
        bestemming (str): The destination of the ride
        plaats_bestemming (str): The place of the destination
        vias (str): The vias of the ride
        dienstregeling_tijdstip (str): The schedule time of the ride
        links (list[Link]): The links to other resources related to the passage
    """

    entiteitnummer: int
    lijnnummer: int
    richting: str
    ritnummer: int
    bestemming: str
    plaats_bestemming: str = Field(validation_alias="plaatsBestemming")
    vias: list[str] | None = None
    # TODO: Properly parse the datetime
    dienstregeling_tijdstip: str = Field(validation_alias="dienstregelingTijdstip")


class Dienstregeling(BaseModel):
    """Represents a schedule

    Attributes:
        doorkomsten (list[Doorkomst]): The passages of the schedule
        doorkomst_notas (list[DoorkomstNota]): The notes of the passages of the schedule
        rit_notas (list[RitNota]): The notes of the rides of the schedule
        dienstregeling_notas (list[DienstregelingNota]): The notes of the schedule
    """

    doorkomsten: list[Doorkomst]
    doorkomst_notas: list[DoorkomstNota]
    rit_notas: list[RitNota]


class GeoCoordinate(BaseModel):
    """Represents a geographical coordinate

    Attributes:
        latitude (float): The latitude of the coordinate
        longitude (float): The longitude of the coordinate
    """

    latitude: float
    longitude: float


class HalteInDeBuurt(BaseModel):
    """Represents a stop in the neighborhood of a given geo-coordinate

    Attributes:
        type (str): The type of the stop
        id (str): The ID of the stop
        naam (str): The name of the stop
        afstand (int): The distance to the stop
        geo_coordinaat (GeoCoordinaat): The geographical coordinate of the stop
        links (list[Link]): The links to other resources related to the stop
    """

    type: str
    id: int
    naam: str
    afstand: int
    geo_coordinate: GeoCoordinate = Field(validation_alias="geoCoordinaat")


class Vervoerregio(BaseModel):
    """Represents a transport region in Belgium

    Attributes:
        code (str): The code of the transport region
        naam (str): The name of the transport region
        nr (str): The number of the transport region
        links (list[Link]): The links to other resources related to the transport region
    """

    code: str
    naam: str
    nr: int


class RGB(BaseModel):
    """Represents a color

    Attributes:
        rood (int): The red value of the color
        groen (int): The green value of the color
        blauw (int): The blue value of the color
    """

    rood: int
    groen: int
    blauw: int


class Kleur(BaseModel):
    """Represents a color

    Attributes:
        hex (str): The hex code of the color
    """

    code: str
    omschrijving: str
    rgb: RGB
    hex: str


class Lijn(BaseModel):
    """Represents a line in Belgium

    Attributes:
        lijnnummer (str): The number of the line
        omschrijving (str): The description of the line
        entiteitnummer (str): The number of the entity
        links (list[Link]): The links to other resources related to the line
    """

    entiteitnummer: int
    lijnnummer: int
    lijnnummer_publiek: str = Field(validation_alias="lijnnummerPubliek")
    omschrijving: str
    vervoer_regio_code: str = Field(validation_alias="vervoerRegioCode")
    publiek: bool
    vervoertype: str
    bedieningtype: str
    lijn_geldig_van: date = Field(validation_alias="lijnGeldigVan")
    lijn_geldig_tot: date = Field(validation_alias="lijnGeldigTot")


class Halte(BaseModel):
    """Represents a stop in Belgium

    Attributes:
        entiteitnummer (str): The number of the entity
        haltenummer (str): The number of the stop
        omschrijving (str): The description of the stop
        omschrijving_lang (str): The long description of the stop
        district_code (str): The code of the district
        taal (str): The language of the stop
        gemeentenummer (int): The number of the municipality
        omschrijving_gemeente (str): The description of the municipality
        geo_coordinaat (GeoCoordinaat): The geographical coordinate of the stop
        halte_toegankelijkheden (str): The accessibility of the stop
        hoofd_halte (bool): Whether the stop is the main stop
        links (list[Link]): The links to other resources related to the stop
    """

    entiteitnummer: int
    haltenummer: int
    omschrijving: str
    omschrijving_lang: str = Field(validation_alias="omschrijvingLang")
    taal: str
    gemeentenummer: int
    omschrijving_gemeente: str = Field(validation_alias="omschrijvingGemeente")
    geo_coordinaat: GeoCoordinate = Field(validation_alias="geoCoordinaat")
    halte_toegankelijkheden: list[str] = Field(
        validation_alias="halteToegankelijkheden"
    )
    hoofd_halte: bool | None = Field(default=None, validation_alias="hoofdHalte")


class Entiteit(BaseModel):
    """Represents an entity in Belgium

    Attributes:
        entiteitnummer (int): The number of the entity
        entiteitcode (str): The code of the entity
        omschrijving (str): The description of the entity
        links (list[Link]): The links to other resources related to the entity
    """

    entiteitnummer: int
    entiteitcode: str
    omschrijving: str


class HoofdGemeente(BaseModel):
    """Represents a main municipality in Belgium

    Attributes:
        hoofdgemeentenummer (int): The number of the main municipality
        omschrijving (str): The description of the main municipality
    """

    hoofdgemeentenummer: int
    omschrijving: str


class Gemeente(BaseModel):
    """Represents a municipality in Belgium

    Attributes:
        gemeentenummer (int): The number of the municipality
        omschrijving (str): The description of the municipality
        hoofd_gemeente (HoofdGemeente | None, optional): The main municipality of the municipality. Defaults to None.
        links (list[Link]): The links to other resources related to the municipality
    """

    gemeentenummer: int
    omschrijving: str
    # TODO: https://docs.pydantic.dev/latest/concepts/fields/#field-aliases
    hoofd_gemeente: HoofdGemeente | None = None
