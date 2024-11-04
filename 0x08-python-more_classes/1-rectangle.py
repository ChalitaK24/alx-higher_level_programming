#!/usr/bin/python3

class Rectangle:


    def __init__(self,width, height):
        self.width = width
        self.height = height

    def width(self):
        return self.__width


    def width(self, value):
        if not is instance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
