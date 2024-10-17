#!/usr/bin/python3

"""function to check if obj is instance of inherited class"""


def is_kind_of_class(obj, a_class):
    """
    Returns True, if the obj is an instance of the class
    """

    return isinstance(obj, a_class)
