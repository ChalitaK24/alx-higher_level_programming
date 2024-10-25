#!/usr/bin/python3

""" Class Rectangle that inherits from Base"""

from models.base import Base

""" Class Rectangle"""


class Rectangle(Base):
    """
    Implementation of Class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter
        """

        if type(value) is not int or value <= 0:
            raise ValueError("width must be a positive int")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """

        if type(value) is not int or value <= 0:
            raise ValueError("height must be Posisitve int")
        self.__height = value

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        """
        if type(value) is not int or value < 0:
            raise ValueError("x must be non-negative int")
        self.__x = value

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        """
        if type(value) is not int or value < 0:
            raise ValueError("y must be a non-negative int")
        self.__y = value
