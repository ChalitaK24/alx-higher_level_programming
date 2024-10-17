#!/usr/bin/python3

"""Function checks if the obj is an instance of the specified class"""


def is_same_class(obj, a_class):
    """
    Returns: True if the object is exaxtly an instance of the specified class
    """
    return type(obj) == a_class
