#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_invalid_width_type(self):
        """Test TypeError when width is not an integer."""
        with self.assertRaises(TypeError) as context:
            Rectangle("10", 5)  # Attempt to instantiate with a string as width
        self.assertEqual(str(context.exception), "width must be an integer")  # Check the exception message

    def test_invalid_height_type(self):
        """Test TypeError when height is not an integer."""
        with self.assertRaises(TypeError) as context:
            Rectangle(10, "5")  # Attempt to instantiate with a string as height
        self.assertEqual(str(context.exception), "height must be an integer")  # Check the exception message

# More test cases can follow...

if __name__ == "__main__":
    unittest.main()

