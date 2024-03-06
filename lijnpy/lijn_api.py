import os
from logging import Logger, getLogger

from pydantic import ValidationError

from lijnpy.exceptions import DeLijnAPIException
from lijnpy.models import Gemeenten
from lijnpy.rest_adapter import RestAdapter


class KernOpenDataServicesAPI:
    def __init__(
        self,
        hostname: str = "api.delijn.be/DLKernOpenData/api",
        api_key: str = "",
        ver: str = "v1",
        ssl_verify: bool = True,
        logger: Logger | None = None,
    ):
        """
        Constructor for KernOpenDataServicesAPI

        Args:
            hostname (str, optional): The hostname of the API. Defaults to "api.delijn.be/DLKernOpenData".
            api_key (str, optional): The API key to use for authentication. Defaults to "".
            ver (str, optional): The version of the API to use. Defaults to "v1".
            ssl_verify (bool, optional): Whether to verify the SSL certificate. Defaults to True.
            logger (Logger | None, optional): The logger to use for logging. Defaults to None.
        """
        self._rest_adapter = RestAdapter(hostname, api_key, ver, ssl_verify, logger)
        self._logger = logger or getLogger(__name__)

    def get_gemeenten(self) -> Gemeenten:
        """Get a list of all municipalities in Belgium

        Returns:
            Result: The result of the request
        """
        result = self._rest_adapter.get("/gemeenten")
        try:
            assert result.data is not None
            gemeenten = Gemeenten(**result.data)
        except (AssertionError, ValidationError) as e:
            self._logger.error(f"Failed to parse the response from the API: {e}")
            raise DeLijnAPIException from e

        return gemeenten


print(KernOpenDataServicesAPI(api_key=os.environ["DELIJN_API_KEY"]).get_gemeenten())
