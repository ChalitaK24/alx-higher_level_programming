#!/usr/bin/python3

import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setup(self):
        Rectangle._Base__nb_objects = 0

    def test_class_exists(self):
        self.assertIsNotNone(Rectangle)

    def test_create_instance_without_id(self):
        r = Rectangle(5, 10)
        self.asserIsInstance(r, Rectangle)

    def test_create_instance_with_id(self):
        r = Rectangle(5, 10, 0, 0, 99)
        self.assertEqual(r.id, 99)

    def test_getters_setters(self):
        r = rectangle(5, 10, 2, 3)
        self.assertEqual(r.width, 5)
        self.asserEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

    def test_invalid_height(self):
        with self.assert Raises(ValueError):
            Rectangle(5, -10)

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1, 0)

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 0, -1)
""" qn 3"""


    def test_invalid_width_type(self):

        with self.assertRaises(TypeError) as context:
            Rectangle("10", 5)

        self.assertEqual(str(context.exception), "width must be an integer")  

    def test_invalid_height_type(self):

        with self.assertRaises(TypeError) as context:
            Rectangle(10, "5")

        self.assertEqual(str(context.exception), "height must be an integer")

""" question 4"""

    def test_area(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)


""" qn 5"""

    def test_display(self):
        r = rectangle(4, 3)

        captured_output = StringID()
        sys.stdout = captured_output

        r.display()

        sys.stdout = sys.__stdout__

        expected_output = "####\n####\n####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

""" qn 6"""
    
    def test_str_method(self):
        r = Rectangle(4, 3, 2, 1, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 2/1 - 4/3")

""" qn 7"""
    
    def test_display(self):
        r = Rectangle(4, 3, 2, 1)
        expected_output = "\n  ####\n  ####\n  ####\n"

        captured_output = StringIO()
        sys.stdout = captured_output

        r.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

""" qn 9"""
    def test_update_args(self):
        
        r = Rectangle(4, 3, 0, 0)
        r.update(10, 6, 2, 3, 4)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_kwargs(self):

        r = Rectangle(4, 3, 0, 0)
        r.update(width=8, height=5, x=1, y=2)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_update_args_and_kwargs(self):

        r = Rectangle(4, 3, 0, 0)
        r.update(10, 6, 2, 3, 4, width=9, height=7)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

if __name__ == "__main__":
    unittest.main()
