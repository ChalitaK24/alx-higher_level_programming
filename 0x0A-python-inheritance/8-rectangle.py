#!/usr/bin/python3

"""
Rectangle class that inherits from BaseGeometry
"""
class BaseGeometry:
    """
    A class with geometry utilities
    """
    
    def area(self):
        """

        """
        reaise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """

        """
        if not isinstance(value, int):
            raise TypeError:(f"{name} must be in an integer")
        if value < 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """

    """
    def __init__(self, width, height):
        """

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
