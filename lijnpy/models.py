from typing import Any

from pydantic import BaseModel


class Result(BaseModel):
    """The result of a request to the De Lijn API

    Attributes:
        status_code (int): The status code of the request
        message (str, optional): The message of the request. Defaults to "".
        data (dict[str, Any] | None, optional): The data of the request. Defaults to None.
    """

    status_code: int
    message: str = ""
    data: dict[str, Any] | None = None


class Link(BaseModel):
    """Represents a link to a resource

    Attributes:
        rel (str): How the resource is related to the current resource
        url (str): The URL of the resource
    """

    rel: str
    url: str


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
    hoofd_gemeente: HoofdGemeente | None = None
    links: list[Link]


class Gemeenten(BaseModel):
    """Represents a list of municipalities in Belgium

    Attributes:
        gemeenten (list[Gemeente]): The list of municipalities
        links (list[Link]): The links to other resources related to this endpoint
    """

    gemeenten: list[Gemeente]
    links: list[Link]


class Entiteit(BaseModel):
    """Represents an entity in Belgium

    Attributes:
        entiteitnummer (str): The number of the entity
        entiteitcode (str): The code of the entity
        omschrijving (str): The description of the entity
        links (list[Link]): The links to other resources related to the entity
    """

    entiteitnummer: str
    entiteitcode: str
    omschrijving: str
    links: list[Link]


class GeoCoordinaat(BaseModel):
    """Represents a geographical coordinate

    Attributes:
        latitude (float): The latitude of the coordinate
        longitude (float): The longitude of the coordinate
    """

    latitude: float
    longitude: float


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

    entiteitnummer: str
    haltenummer: str
    omschrijving: str
    omschrijving_lang: str
    taal: str
    gemeentenummer: int
    omschrijving_gemeente: str
    geo_coordinaat: GeoCoordinaat
    halte_toegankelijkheden: list[str]
    hoofd_halte: bool | None = None
    links: list[Link]


class Lijn(BaseModel):
    """Represents a line in Belgium

    Attributes:
        lijnnummer (str): The number of the line
        omschrijving (str): The description of the line
        entiteitnummer (str): The number of the entity
        links (list[Link]): The links to other resources related to the line
    """

    entiteitnummer: str
    lijnnummer: str
    lijnnummer_publiek: str
    omschrijving: str
    vervoer_regio_code: str
    publiek: bool
    vervoertype: str
    bedieningtype: str
    lijn_geldig_van: str
    lijn_geldig_tot: str
    links: list[Link]


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
    links: list[Link]


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
    nr: str
    links: list[Link]
