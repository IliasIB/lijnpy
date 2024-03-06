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
