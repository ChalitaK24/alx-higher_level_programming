#!/usr/bin/python3

import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_invalid_width_type(self):
        """Test TypeError when width is not an integer."""
        with self.assertRaises(TypeError) as context:
            Rectangle("10", 5)

        self.assertEqual(str(context.exception), "width must be an integer")  

    def test_invalid_height_type(self):
        """Test TypeError when height is not an integer."""
        with self.assertRaises(TypeError) as context:
            Rectangle(10, "5")

        self.assertEqual(str(context.exception), "height must be an integer")

if __name__ == "__main__":
    unittest.main()
