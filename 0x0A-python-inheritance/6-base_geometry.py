#!/usr/bin/python3

"""Function defines class with unimplemented area method"""


class BaseGeometry:
    """
    Class defines BaseGeometry with unimplemented area mtd
    """

    def area(self):
        """
         Raises an Exception indicating that the area mtd  is not implemented
         """
        raise Exception("area() is not implemented")
