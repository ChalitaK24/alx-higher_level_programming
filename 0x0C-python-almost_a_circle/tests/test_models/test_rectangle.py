#!/usr/bin/python3

import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        """Reset __nb_objects to ensure a consistent test environment."""
        Rectangle._Base__nb_objects = 0

    def test_class_exists(self):
        """Test that the Rectangle class exists."""
        self.assertIsNotNone(Rectangle)

    def test_create_instance_without_id(self):
        """Test creating a Rectangle instance without an id."""
        r = Rectangle(5, 10)
        self.assertIsInstance(r, Rectangle)

    def test_create_instance_with_id(self):
        """Test creating a Rectangle instance with a provided id."""
        r = Rectangle(5, 10, 0, 0, 99)
        self.assertEqual(r.id, 99)

    def test_auto_assign_id(self):
        """Test automatic id assignment when no id is provided."""
        r1 = Rectangle(5, 10)
        r2 = Rectangle(7, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_getters_setters(self):
        """Test getters and setters for width, height, x, and y."""
        r = Rectangle(5, 10, 2, 3)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_invalid_width(self):
        """Test ValueError when width is invalid."""
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

    def test_invalid_height(self):
        """Test ValueError when height is invalid."""
        with self.assertRaises(ValueError):
            Rectangle(5, -10)

    def test_invalid_x(self):
        """Test ValueError when x is invalid."""
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1, 0)

    def test_invalid_y(self):
        """Test ValueError when y is invalid."""
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 0, -1)

if __name__ == "__main__":
    unittest.main()

