#!/usr/bin/python3

""" Implementing Base class."""


class Base:

    """ Private class atribute. """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Class constructor function.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects