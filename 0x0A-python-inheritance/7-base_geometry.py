#!/usr/bin/python3

"""Function that raises execption and validates int for class"""


class BaseGeometry:
    """
    class that defines with methods for calculating area and validating int
    """
    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validation(self, name, value):
        """
         name (str): The name of the parameter.
         value (int): The value to validate.
         Raises:
         TypeError: If value is not an int
         ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
