"""
Module for wrapping around the memoQ server Web Service API

This library is being developed against v9.2.5 of the memoQ API documentation.  The latest version of the API
documentation can be found here:

https://docs.memoq.com/current/api-docs/wsapi/

This code is released under the MIT License.
"""
from abc import ABC, abstractmethod
from urllib.parse import urljoin

from zeep import CachingClient  # https://python-zeep.readthedocs.io/en/master/client.html#caching-of-wsdl-and-xsd-files


DEFAULT_BASE_URL = 'http://localhost:8080'


class MemoQWebServiceBase(ABC):
    """
    Abstract Base Class for memoQ Web Service API Services.
    """

    def __init__(self, base_url: str = None):
        """
        Initializer for the class.

        :param base_url: Base URL of the memoQ Web Service API, as a string.  For example: "http://localhost:8080"
        """
        self.base_url = base_url if base_url is not None else DEFAULT_BASE_URL
        self.__client = CachingClient(wsdl=self.service_url)

    def __dir__(self) -> list:
        """
        Method for getting a list of attributes associated with the object.

        Since we override __getattr__ to forward attribute lookups to the underlying client, we also override this
        method so we can include the list of attributes of the underlying client.

        :returns: List of attributes, as a list of strings.
        """
        return sorted(set(
            super().__dir__() +
            list(self.__dict__.keys()) +
            self.__client.service.__dir__()
        ))

    def __getattr__(self, item):
        """
        Method for forwarding attribute lookups to the underlying client service.

        :param item: Item attribute to lookup.
        """
        return getattr(self.__client.service, item)

    @property
    @abstractmethod
    def service_url(self) -> str:
        """
        Method for getting the service URL associated with the object.

        :returns: The service URL associated with the object, as a string.
        """
        raise NotImplementedError


class MemoQAsynchronousTasksService(MemoQWebServiceBase):
    """
    Class for the Asynchronous Tasks management API.

    The latest version of the API documentation for the Asynchronous Tasks management API can be found here:

    https://docs.memoq.com/current/api-docs/wsapi/memoqservices/tasksservice.html
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
        Method for getting the service URL associated with the Asynchronous Tasks management endpoint.

        :returns: The service URL associated with the Asynchronous Tasks management endpoint, as a string.
        """
        return urljoin(self.base_url, '/memoqservices/tasks?wsdl')


class MemoQELMService(MemoQWebServiceBase):
    """
    Class for the License (ELM) management API.

    The latest version of the API documentation for the License (ELM) management API can be found here:

    https://docs.memoq.com/current/api-docs/wsapi/memoqservices/elmservice.html
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
        Method for getting the service URL associated with the License (ELM) management endpoint.

        :returns: The service URL associated with the License (ELM) management endpoint, as a string.
        """
        return urljoin(self.base_url, '/memoqservices/elm?wsdl')


class MemoQFileManagerService(MemoQWebServiceBase):
    """
    Class for the File Manager service API.

    The latest version of the API documentation for the File Manager service API can be found here:

    https://docs.memoq.com/current/api-docs/wsapi/memoqservices/filemanagerservice.html
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
        Method for getting the service URL associated with the File Manager service endpoint.

        :returns: The service URL associated with the File Manager service endpoint, as a string.
        """
        return urljoin(self.base_url, '/memoqservices/filemanager?wsdl')


class MemoQLightResourceService(MemoQWebServiceBase):
    """
    Class for the Light resource management API.

    The latest version of the API documentation for the Light resource management API can be found here:

    https://docs.memoq.com/current/api-docs/wsapi/memoqservices/lightresourceservice.html
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
        Method for getting the service URL associated with the Light resource management endpoint.

        :returns: The service URL associated with the Light resource management endpoint, as a string.
        """
        return urljoin(self.base_url, '/memoqservices/resource?wsdl')


class MemoQLiveDocsService(MemoQWebServiceBase):
    """
    Class for the LiveDocs management API.

    The latest version of the API documentation for the LiveDocs management API can be found here:

    https://docs.memoq.com/current/api-docs/wsapi/memoqservices/livedocsservice.html
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
        Method for getting the service URL associated with the LiveDocs management endpoint.

        :returns: The service URL associated with the LiveDocs management endpoint, as a string.
        """
        return urljoin(self.base_url, '/memoqservices/livedocs?wsdl')


class MemoQSecurityService(MemoQWebServiceBase):
    """
    Class for the Security service API.

    The latest version of the API documentation for the Security service API can be found here:

    https://docs.memoq.com/current/api-docs/wsapi/memoqservices/securityservice.html
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
        Method for getting the service URL associated with the Security service endpoint.

        :returns: The service URL associated with the Security service endpoint, as a string.
        """
        return urljoin(self.base_url, '/memoqservices/security?wsdl')


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
        Method for getting the service URL associated with the Server project management endpoint.

        :returns: The service URL associated with the Server project management endpoint, as a string.
        """
        return urljoin(self.base_url, '/memoqservices/serverproject?wsdl')


class MemoQTBService(MemoQWebServiceBase):
    """
    Class for the Term base API.

    The latest version of the API documentation for the Term base API can be found here:

    https://docs.memoq.com/current/api-docs/wsapi/memoqservices/tbservice.html
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
        Method for getting the service URL associated with the Term base management endpoint.

        :returns: The service URL associated with the Term base management endpoint, as a string.
        """
        return urljoin(self.base_url, '/memoqservices/tb?wsdl')


class MemoQTMService(MemoQWebServiceBase):
    """
    Class for the Translation Memory API.

    The latest version of the API documentation for the Translation Memory API can be found here:

    https://docs.memoq.com/current/api-docs/wsapi/memoqservices/tmservice.html
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
        Method for getting the service URL associated with the Translation Memory management endpoint.

        :returns: The service URL associated with the Translation Memory management endpoint, as a string.
        """
        return urljoin(self.base_url, '/memoqservices/tm?wsdl')
