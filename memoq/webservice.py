"""
Module for wrapping around the memoQ server Web Service API

The latest version of the API documentation can be found here:

https://docs.memoq.com/current/api-docs/wsapi/

This code is released under the MIT License.
"""
from abc import ABC, abstractmethod
from urllib.parse import urljoin

from zeep import Client


class MemoQWebServiceBase(ABC):
    """
    Abstract Base Class for memoQ Web Service API Services.
    """

    def __init__(self, base_url: str = None):
        """
        Initializer for the class.

        :param base_url: Base URL of the memoQ Web Service API, as a string.  For example: "http://localhost:8080"
        """
        if base_url is not None:
            self.base_url = base_url
        else:
            self.base_url = "http://localhost:8080"
        self.__client = Client(wsdl=self.service_url)

    def __getattr__(self, item):
        """
        Method for forwarding attribute lookups to the underlying client.

        :param item: Item attribute to lookup.
        """
        return getattr(self.__client, item)

    @property
    @abstractmethod
    def service_url(self) -> str:
        """
        Method for getting the service URL associated with the object.

        :return: The service URL associated with the object, as a string.
        """
        raise NotImplementedError


class MemoQServerProjectService(MemoQWebServiceBase):
    """
    Class for the Server project API.

    The latest version of the API documentation for the Server project API can be found here:

    https://docs.memoq.com/current/api-docs/wsapi/memoqservices/serverprojectservice.html
    """

    def __init__(self, base_url: str = None):
        """
        Initializer for the class.

        :param base_url: Base URL of the memoQ Web Service API, as a string.  For example: "http://localhost:8080"
        """
        super().__init__(base_url)

    @property
    def service_url(self) -> str:
        """
        Method for getting the service URL associated with the Server project endpoint.

        :return: The service URL associated with the Server project endpoint, as a string.
        """
        return urljoin(self.base_url, '/memoqservices/serverproject')
