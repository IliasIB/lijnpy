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
