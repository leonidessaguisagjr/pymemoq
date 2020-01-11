"""
Module for wrapping around a memoQ server.

This code is released under the MIT License.
"""
from .webservice import MemoQLiveDocsService, MemoQTBService, MemoQTMService, MemoQSecurityService, \
    MemoQServerProjectService


class MemoQServer(object):
    """Class that represents a memoQ server."""

    def __init__(self, base_url: str):
        """
        Initializer for the class.

        :param base_url: Base URL for the memoQ server.  For example, 'http://localhost:8080'
        """
        self.base_url = base_url
        self._api_endpoints = {}

    def __repr__(self) -> str:
        """
        Method for retrieving a string representing the memoQ server.

        :returns: A str representing the memoQ server.
        """
        return f"{self.__class__.__qualname__}(base_url='{self.base_url}')"

    def __str__(self) -> str:
        """
        Method for retrieving a user-readable string representing the memoQ server.

        :returns: A user readable str for the memoQ server.
        """
        return f"memoQ server v{self.api_version} @ {self.base_url}"

    @property
    def _live_docs_service(self):
        live_docs_service_key = "_live_docs_service"
        try:
            return self._api_endpoints[live_docs_service_key]
        except KeyError:
            self._api_endpoints[live_docs_service_key] = MemoQLiveDocsService(self.base_url)
            return self._api_endpoints[live_docs_service_key]

    @property
    def _security_service(self):
        security_service_key = "_security_service"
        try:
            return self._api_endpoints[security_service_key]
        except KeyError:
            self._api_endpoints[security_service_key] = MemoQSecurityService(self.base_url)
            return self._api_endpoints[security_service_key]

    @property
    def _server_project_service(self):
        server_project_service_key = "_server_project_service"
        try:
            return self._api_endpoints[server_project_service_key]
        except KeyError:
            self._api_endpoints[server_project_service_key] = MemoQServerProjectService(self.base_url)
            return self._api_endpoints[server_project_service_key]

    @property
    def _tb_service(self):
        tb_service_key = "_tb_service"
        try:
            return self._api_endpoints[tb_service_key]
        except KeyError:
            self._api_endpoints[tb_service_key] = MemoQTBService(self.base_url)
            return self._api_endpoints[tb_service_key]

    @property
    def _tm_service(self):
        tm_service_key = "_tm_service"
        try:
            return self._api_endpoints[tm_service_key]
        except KeyError:
            self._api_endpoints[tm_service_key] = MemoQTMService(self.base_url)
            return self._api_endpoints[tm_service_key]

    @property
    def api_version(self) -> str:
        """
        Method for retrieving the API version.  The API version is the version of the memoQ server.

        :returns: The API version, as a string.
        """
        return self._server_project_service.GetApiVersion()

    @property
    def corpora(self) -> list:
        """
        Method for retrieving the list of corpora published by the memoQ server.

        :returns: A list of corpora published by the memoQ server.
        """
        return self._live_docs_service.ListCorpora()

    @property
    def groups(self) -> list:
        """
        Method for retrieving the list of memoQ server groups.

        :returns: A list of memoQ server groups.
        """
        return self._security_service.ListGroups()

    @property
    def projects(self) -> list:
        """
        Method for retrieving the list of projects on the memoQ server.

        :returns: A list of projects on the memoQ server.
        """
        return self._server_project_service.ListProjects()

    @property
    def tbs(self) -> list:
        """
        Method for retrieving the list of all Term Bases (TBs) on the memoQ server.

        :returns: A list of all TBs on the memoQ server.
        """
        return self._tb_service.ListTBs()

    @property
    def tms(self) -> list:
        """
        Method for retrieving the list of all Translation Memories (TMs) on the memoQ server.

        :returns: A list of all TMs on the memoQ server.
        """
        return self._tm_service.ListTMs()

    @property
    def users(self) -> list:
        """
        Method for retrieving the list of memoQ server users.

        :returns: A list of memoQ server users.
        """
        return self._security_service.ListUsers()
