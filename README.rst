``pymemoq``
===========

Python module to facilitate accessing the `memoQ API <https://www.memoq.com/integrations/apis>`_.


Installation
------------

This module is available on the Python Package Index (PyPI) and can be installed as follows:

``pip install pymemoq``


Dependencies
------------

This module is dependent on the following additional packages:

- `zeep <https://pypi.org/project/zeep/>`_


Available classes
-----------------

The following classes are currently available (eventual goal is to provide wrappers for all of the APIs):

Under ``memoq.server``:

 - ``MemoQServer`` - Wraps around a memoQ server and exposes a limited subset of the API

Under ``memoq.webservice``:

 - ``MemoQAsynchronousTasksService`` - Asynchronous Tasks management API
 - ``MemoQELMService`` - License (ELM) management API
 - ``MemoQFileManagerService`` - File upload/download API
 - ``MemoQLightResourceService`` - Light resource management API
 - ``MemoQLiveDocsService`` - LiveDocs management API
 - ``MemoQSecurityService`` - Security API
 - ``MemoQServerProjectService`` - Server projects API
 - ``MemoQTBService`` - Term base management API
 - ``MemoQTMService`` - Translation memory management API


Example API Usage
-----------------
    >>> from memoq import MemoQServer
    >>> memoq_server = MemoQServer('http://localhost:8080')
    >>> memoq_server.api_version
    '9.2.5'
    >>> from memoq.webservice import MemoQServerProjectService
    >>> project_service = MemoQServerProjectService('http://localhost:8080')
    >>> project_service.GetApiVersion()
    '9.2.5'
    >>> from memoq.util import response_object_to_dict
    >>> projects = [response_object_to_dict(project) for project in memoq_server.projects]
    >>> from collections import Counter
    >>> Counter([proj['DocumentStatus'] for proj in projects])
    Counter({'TranslationInProgress': 12, 'TranslationFinished': 34, 'ProofreadingFinished': 56})
    >>>

Implementation Notes
--------------------

Per the recommendation to `enable caching of WSDL and XSD files
<https://python-zeep.readthedocs.io/en/master/client.html#caching-of-wsdl-and-xsd-files>`_, we are using an instance of
the ``zeep.CachingClient()`` under the hood.  Since the memoQ WSDL and XSD files should not be changing except when
the server is upgraded, this should improve performance without causing any issues.


References
----------
 - `memoQ Server Resources API documentation <https://docs.memoq.com/current/api-docs/resapi/APIHelp.html>`_
 - `memoQ server Web Service API documentation <https://docs.memoq.com/current/api-docs/wsapi/>`_


License
-------

This is released under an MIT license.  See the ``LICENSE`` file in this repository for more information.
