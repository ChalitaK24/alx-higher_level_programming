#!/usr/bin/python3

"""creaste Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """
        new Square instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns str representation
        of tha Square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Get size of the Square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Get size of Square
        """
        self.width = value
        self.height = value
