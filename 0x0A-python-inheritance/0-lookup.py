#!/usr/bin/python3

"""Function Returns a list of available attr and mtd of obj"""


def lookup(obj):
    """
    obj: the object to inspect
    Returns: list of attr and mtds available in obj
    """

    return dir(obj)
