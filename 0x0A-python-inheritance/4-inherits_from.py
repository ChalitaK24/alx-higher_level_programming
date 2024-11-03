#!/usr/bin/python3

"""Function to check if an obj is an instance of inherited class"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
