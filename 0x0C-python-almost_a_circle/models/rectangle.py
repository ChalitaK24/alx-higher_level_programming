#!/usr/bin/python3

""" Class Rectangle that inherits from Base"""

from models.base import Base

""" class Rectangle"""

    def __init_(slef, width, height, x=0, y=0, id=None):
        """
        Function calls Class constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def width(self):
        """
        Width getter
        """
        return self.__width

    def width(self, value):
        """
        Width setter
        """

        if type(value) is not int or value <= 0:
            raise ValueError("width must be a positive int")
        self.__width = value


    def height(self):
        """
        height getter
        """
        return self.__height

    def height(self, value):
        """
        height setter
        """

        if type(value) is not int or value <= 0:
            raise ValueError("height must be Posisitve int")
        self.__height = value

    def x(self):
        """
        x getter
        """
        return self.__x

    def x(self, value):
        """
        x setter
        """
        if type(value) is not int or value < 0:
            raise ValueError("x must be non-negative int")
        self.__x = value


    def y(self):
        """
        y getter
        """
        return self.__y


    def y(self, value): 
        """
        y setter
        """
        if type(value) is not int or value < 0:
            raise ValueErrorr("y must be a non-negative int")
        self.__y = value
