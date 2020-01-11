"""
Module for utility functions.

This code is released under the MIT License.
"""
from zeep.helpers import serialize_object


def response_object_to_dict(o: object) -> dict:
    """
    The response objects that come back from the memoQ web service API call are zeep objects.  This utility function
    simply serializes the object into a standard dict.

    :param o: The object to serialize
    :returns: The object, serialized as a standard dict.
    """
    return serialize_object(o, target_cls=dict)
