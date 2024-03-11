from __future__ import annotations

from pydantic import BaseModel, Field, HttpUrl


class Link(BaseModel):
    """Represents a link

    Attributes:
        relation (str): The relation of the link
        url (str): The URL of the link
    """

    relation: str = Field(validation_alias="rel")
    url: HttpUrl = Field(validation_alias="url")


class GeoCoordinate(BaseModel):
    """Represents a geographical coordinate

    Attributes:
        latitude (float): The latitude of the coordinate
        longitude (float): The longitude of the coordinate
    """

    latitude: float
    longitude: float


class DetourPeriod(BaseModel):
    """Represents a period of a detour of a line

    Attributes:
        start_date (str): The start date of the period
        end_date (str, optional): The end date of the period. Defaults to None.
    """

    start_date: str = Field(validation_alias="startDatum")
    end_date: str | None = Field(default=None, validation_alias="eindDatum")
