#!/usr/bin/python3

import unittest
from models.square import Square
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO

class TestSquare(unittest.TestCase):

"""qn 10"""

    def test_class_exists_and_inherits_from_rectangle(self):

        self.assertTrue(issubclass(Square, Rectangle))

    def test_create_square_with_only_size(self):

        square = Square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)

    def test_create_square_with_size_and_x(self):

        square = Square(5, 7)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 7)

    def test_create_square_with_size_x_and_y(self):

        square = Square(5, 7, 2)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 2)

    def test_create_square_with_size_x_y_and_id(self):

        square = Square(5, 7, 2, 89)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 89)

    def test_str_method_is_overloaded(self):

        square = Square(5, 7, 2, 89)
        self.assertEqual(str(square), "[Square] (89) 7/2 - 5")

    def test_area_method_exists(self):

        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_display_method_exists(self):

        square = Square(3)
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            square.display()
            output = mock_stdout.getvalue()
        self.assertIn("#", output)

""" question    """

    def test_str_method_is_overloaded(self):

        square = Square(5, 7, 2, 89)
        self.assertEqual(str(square), "[Square] (89) 7/2 - 5")

if __name__ == '__main__':
    unittest.main()



"""question 12"""

class TestSquareUpdateMethod(unittest.TestCase):

    def test_update_with_args(self):
        """Test update with *args to set id, size, x, y in order."""
        sq = Square(5)
        sq.update(89, 10, 2, 3)
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)

    def test_update_with_kwargs(self):
        """Test update with **kwargs to set specific attributes."""
        sq = Square(5)
        sq.update(id=100, size=15, y=8)
        self.assertEqual(sq.id, 100)
        self.assertEqual(sq.size, 15)
        self.assertEqual(sq.y, 8)

    def test_update_args_priority_over_kwargs(self):
        """Test that *args is prioritized over **kwargs when both are provided."""
        sq = Square(5)
        sq.update(50, 20, 5, 5, id=99, size=10, x=0, y=0)
        self.assertEqual(sq.id, 50)
        self.assertEqual(sq.size, 20)
        self.assertEqual(sq.x, 5)
        self.assertEqual(sq.y, 5)

    def test_update_only_id_with_args(self):
        """Test that only id is updated when one argument is passed to *args."""
        sq = Square(5)
        sq.update(75)
        self.assertEqual(sq.id, 75)

    def test_update_invalid_keys_in_kwargs(self):
        """Test **kwargs ignores invalid attribute keys."""
        sq = Square(5)
        sq.update(size=20, invalid_attr=100)
        self.assertEqual(sq.size, 20)
        self.assertFalse(hasattr(sq, 'invalid_attr'))

if __name__ == '__main__':
    unittest.main()

"""13th question"""

class TestRectangle(unittest.TestCase):

    def test_to_dictionary(self):
        """Test the dictionary representation of Rectangle."""
        rec = Rectangle(4, 6, 2, 1, 101)
        expected_dict = {
            'id': 101,
            'width': 4,
            'height': 6,
            'x': 2,
            'y': 1
        }
        self.assertEqual(rec.to_dictionary(), expected_dict)

"""14 question"""

class TestSquare(unittest.TestCase):

    def test_square_to_dictionary(self):
        square = Square(5, 2, 3, 10)
        expected_dict = {
            'id': 10,
            'size': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
