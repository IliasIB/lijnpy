from lijnpy.components import Gemeente
from lijnpy.rest_adapter import DeLijnAPI


def gemeentes() -> list[Gemeente]:
    gemeenten = DeLijnAPI.get("/DLKernOpenData/api/v1/gemeenten")
    print(gemeenten)
    return []


gemeentes()
