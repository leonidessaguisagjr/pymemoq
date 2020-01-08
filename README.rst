``pymemoq``
===========

Python module to facilitate accessing the memoQ Web Service API.


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

The following classes are currently available:

Under ``memoq.webservice``:

 - ``MemoQServerProjectService`` - Server projects
 - ``MemoQTBService`` - Term base management
 - ``MemoQTMService`` - Translation memory management


Example API Usage
-----------------

    >>> from memoq.webservice import MemoQServerProjectService
    >>> project_service = MemoQServerProjectService('http://localhost:8080')
    >>> project_service.GetApiVersion()
    '9.2.5'
    >>>


License
-------

This is released under an MIT license.  See the ``LICENSE`` file in this repository for more information.
