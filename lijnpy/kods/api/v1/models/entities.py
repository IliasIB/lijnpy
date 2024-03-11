from __future__ import annotations

from datetime import date

from pydantic import BaseModel, Field

from lijnpy.kods.api.v1.models.utils import GeoCoordinate, Link


class EntityResponse(BaseModel):
    """Represents a response from the entity API

    Attributes:
        number (int): The number of the entity
        code (str): The code of the entity
        description (str): The description of the entity
    """

    number: int = Field(validation_alias="entiteitnummer")
    code: str = Field(validation_alias="entiteitcode")
    description: str = Field(validation_alias="omschrijving")
    links: list[Link] = Field(validation_alias="links")


class EntitiesResponse(BaseModel):
    """Represents a response from the entities API

    Attributes:
        entities (list[Entity]): The entities of the response
        links (list[Link]): The links of the response
    """

    class Entity(BaseModel):
        number: int = Field(validation_alias="entiteitnummer")
        code: str = Field(validation_alias="entiteitcode")
        description: str = Field(validation_alias="omschrijving")
        links: list[Link] = Field(validation_alias="links")

    entities: list[Entity] = Field(validation_alias="entiteiten")
    links: list[Link] = Field(validation_alias="links")


class MunicipalitiesResponse(BaseModel):
    """Represents a response from the municipalities API

    Attributes:
        municipalities (list[MunicipalityResponse]): The municipalities of the response
    """

    class Municipality(BaseModel):
        class MainMunicipality(BaseModel):
            number: int = Field(validation_alias="gemeentenummer")
            description: str = Field(validation_alias="omschrijving")

        number: int = Field(validation_alias="gemeentenummer")
        description: str = Field(validation_alias="omschrijving")
        main_municipality: MainMunicipality | None = Field(
            default=None, validation_alias="hoofdGemeente"
        )
        links: list[Link] = Field(validation_alias="links")

    municipalities: list[Municipality] = Field(validation_alias="gemeenten")
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


class LinesResponse(BaseModel):
    """Represents a response from the lines API

    Attributes:
        lines (list[Line]): The lines of the response
    """

    class Line(BaseModel):
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
        links: list[Link] = Field(validation_alias="links")

    lines: list[Line] = Field(validation_alias="lijnen")
    links: list[Link] = Field(validation_alias="links")
