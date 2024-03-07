from pathlib import Path

import requests


def _get_encoded_input(path: str) -> bytes:
    """Gets an input file and returns its contents as bytes.

    Args:
        path (str): The path to the input file.

    Returns:
        bytes: The contents of the input file.
    """
    file_path = Path(path)
    with file_path.open() as file:
        contents = file.read()
    return contents.encode()


def get_good_request_input(path: str) -> requests.Response:
    """Gets an input file and returns it as a Response object with status code 200.

    Args:
        path (str): The path to the input file.

    Returns:
        requests.Response: The input file as a Response object with status code 200.
    """
    response = requests.Response()
    response.status_code = 200
    response.reason = "OK"
    response._content = _get_encoded_input(path)
    return response
