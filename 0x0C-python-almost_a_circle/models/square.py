#!/usr/bin/python3

"""creaste Square class"""

from models.rectangle import Rectangle

""" class Square inherits from rectangle"""


class Square(Rectangle):
    """ class constructor"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        new Square instance.
        """
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """
        returns str representation of the Square
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
        set size of Square
        """
        self.width = value
        self.height = value
 
    def update(self, *args, **kwargs):
        """
        Assigns arg to id, size, x and y attributes

        If *args is provided, assign value
        1st to 4th argument:  id, size, x, y,
        If **kwargs is provided and *args is empty, assign based on key words
        """

        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)

        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        return the dictionary representation of rectangle inst
        """
        return {
            'id': self.id,
            'size': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        } 
