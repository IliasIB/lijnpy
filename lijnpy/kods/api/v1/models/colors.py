from pydantic import BaseModel, Field

from lijnpy.kods.api.v1.models.utils import Link


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


class ColorResponse(BaseModel):
    """Represents a response from the color API

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
    links: list[Link] = Field(validation_alias="links")


class ColorsResponse(BaseModel):
    """Represents a response from the colors API

    Attributes:
        colors (list[Color]): The colors of the response
    """

    class Color(BaseModel):
        code: str
        description: str = Field(validation_alias="omschrijving")
        rgb: RGB
        hex: str

    colors: list[Color] = Field(validation_alias="kleuren")
    links: list[Link] = Field(validation_alias="links")
