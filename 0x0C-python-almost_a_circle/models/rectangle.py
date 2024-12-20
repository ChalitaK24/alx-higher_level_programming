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

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Computes the area of a rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        use # to print rectangle
        """
        for col in range(self.y):
            print("")

        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        returns str representation of rectangle
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Update the rectangle attributes with
        positional or keyword arguments
        """
        if args:
            """
            *args for setting attributes in order
             """
            attr = ["id", "width", "height", "x", "y"]

            for i, arg in enumerate(args):
                if i < len(attr):
                    setattr(self, attr[i], arg)
        else:
            """
            *kwargs to set attributes by name
            if no *args is provided
            """

            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ return the dictionary representaton of Rectangle inst
        """

        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
