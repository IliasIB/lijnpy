from datetime import date

from pydantic import BaseModel, Field

from lijnpy.kods.api.v1.models.utils import Link


class TransportRegionResponse(BaseModel):
    """Represents a transport region in Belgium

    Attributes:
        code (str): The code of the transport region
        name (str): The name of the transport region
        number (str): The number of the transport region
    """

    code: str
    name: str = Field(validation_alias="naam")
    number: int = Field(validation_alias="nr")
    links: list[Link] = Field(validation_alias="links")


class TransportRegionsResponse(BaseModel):
    """Represents a response from the transport regions API

    Attributes:
        transport_regions (list[TransportRegion]): The transport regions of the response
    """

    class TransportRegion(BaseModel):
        code: str
        name: str = Field(validation_alias="naam")
        number: int = Field(validation_alias="nr")
        links: list[Link] = Field(validation_alias="links")

    transport_regions: list[TransportRegion] = Field(validation_alias="vervoerRegios")
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
