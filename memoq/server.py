"""
Module for wrapping around a memoQ server.

This code is released under the MIT License.
"""
from collections.abc import Mapping
from datetime import datetime, timezone

from .webservice import MemoQLightResourceService, MemoQLiveDocsService, MemoQTBService, MemoQTMService, \
    MemoQSecurityService, MemoQServerProjectService


class LightResources(Mapping):
    """Class that represents a mapping of memoQ light resources."""

    def __init__(self, light_resource_service: MemoQLightResourceService):
        """
        Initializer for the class.

        :param light_resource_service: The instance of MemoQLightResourceService to wrap around.
        """
        self._light_resource_service = light_resource_service
        # https://docs.memoq.com/current/api-docs/wsapi/api/lightresourceservice/MemoQServices.ResourceType.html
        self._resource_types = (
            "AutoCorrect", "AutoTrans",
            "FilterConfigs", "FontSubstitution",
            "IgnoreLists",
            "KeyboardShortcuts", "KeyboardShortcuts2",
            "LiveDocsSettings", "LQA",
            "MTSettings",
            "NonTrans",
            "PathRules",
            "ProjectTemplate",
            "QASettings",
            "SegRules",
            "Stopwords",
            "TMSettings",
            "WebSearchSettings"
        )

    def __getitem__(self, item: str) -> list:
        """
        Method for retrieving a light resource.  This essentially wraps around the IResourceService.ListResources()
        method of the memoQ Light resources API.

        For a list of valid Light Resource types to request, see the documentation for MemoQServices.ResourceType:

        https://docs.memoq.com/current/api-docs/wsapi/api/lightresourceservice/MemoQServices.ResourceType.html

        :param item: Light Resource to retrieve, as a str e.g. "ProjectTemplate"
        :returns: A list of Light Resources of the requested type.
        """
        if item in self._resource_types:
            return self._light_resource_service.ListResources(item)
        else:
            raise KeyError(
                f"Unrecognized light resource type.  Valid resource types are: {', '.join(self._resource_types)}")

    def __iter__(self):
        for item in self._resource_types:
            yield item, self[item]

    def __len__(self):
        return len(self._resource_types)


class MemoQServer(object):
    """Class that represents a memoQ server."""

    def __init__(self, base_url: str):
        """
        Initializer for the class.

        :param base_url: Base URL for the memoQ server.  For example, 'http://localhost:8080'
        """
        self.base_url = base_url
        self._all_projects = None
        self._api_endpoints = {}
        self._light_resources = None

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
    def _light_resource_service(self):
        light_resource_service_key = "_light_resource_service"
        try:
            return self._api_endpoints[light_resource_service_key]
        except KeyError:
            self._api_endpoints[light_resource_service_key] = MemoQLightResourceService(self.base_url)
            return self._api_endpoints[light_resource_service_key]

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
    def active_projects(self) -> list:
        """
        Method for retrieving the list of active projects on the memoQ server.

        :returns: A list of active projects on the memoQ server.
        """
        return [proj
                for proj in self.all_projects
                if proj.TimeClosed.replace(tzinfo=timezone.utc) > datetime.now(timezone.utc)]

    @property
    def all_projects(self) -> list:
        """
        Method for retrieving the list of all projects (both active and closed) on the memoQ server.

        :returns: A list of all projects (both active and closed) on the memoQ server.
        """
        # https://docs.memoq.com/current/api-docs/wsapi/api/serverprojectservice/MemoQServices.ServerProjectListFilter.html#MemoQServices_SP_ServerProjectListFilter_TimeClosed
        if self._all_projects is None:
            self._all_projects = self._server_project_service.ListProjects(
                {'TimeClosed': datetime(year=1900, month=1, day=1)})
        return self._all_projects

    @property
    def api_version(self) -> str:
        """
        Method for retrieving the API version.  The API version is the version of the memoQ server.

        :returns: The API version, as a string.
        """
        return self._server_project_service.GetApiVersion()

    @property
    def closed_projects(self) -> list:
        """
        Method for retrieving the list of closed projects on the memoQ server.

        :returns: A list of closed projects on the memoQ server.
        """
        return [proj
                for proj in self.all_projects
                if proj.TimeClosed.replace(tzinfo=timezone.utc) < datetime.now(timezone.utc)]

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
    def light_resources(self) -> LightResources:
        """
        Method for retrieving the list of light resources from the memoQ server.

        :returns: A LightResources instance, suitable for running dict style lookups.
        """
        if self._light_resources is None:
            self._light_resources = LightResources(self._light_resource_service)
        return self._light_resources

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
