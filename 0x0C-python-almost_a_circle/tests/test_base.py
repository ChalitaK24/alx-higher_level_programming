#!/usr/bin/python3

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
    def test_class_exists(self):
        self.assertIsNotNone(Base)
    def test_create_instance_without_id(self):
        b1 = Base()
        self.assertIsInstance(b, Base)
    def test_create_instance_with_id(self):
        b2 = Base(10)
        self.assertEqual(b.id, 10)
    def test_auto_assign_id_without_passing_id(self):
        b = Base()
        self.assertEqual(b.id, 1)
    def test_auto_assign_id_increments(self):
        b3 = Base()
        self.assertEqual(b1.id, 1)
        b4 = Base()
        self.assertEqual(b2.id, 2)

""" question 8"""
    def test_update(self):
        r = Rectangle(4, 3, 0, 0)
        r.update(10, 6, 2, 3, 4)

        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_partial(self):
        r = Rectangle(4, 3, 0, 0)
        r.update(20)

        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

""" question  """


  
"""quetion 15"""

    def test_to_json_string_with_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_with_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

     def test_to_json_string_with_list_of_dicts(self):
        list_dicts = [{"id": 1, "width": 10, "height": 5}]
        json_str = Base.to_json_string(list_dicts)
        expected_str = '[{"id": 1}, {"id": 2, "width": 4}]'
        self.assertEqual(json_str, expected_str)

""" 16"""

     def test_save_to_file(self):
        rectangle = Rectangle(10, 5, 0, 0)
        rectangle2 = Rectangle(7, 3, 1, 1)
        
        Base.save_to_file([rectangle, rectangle2])
        
        with open('Rectangle.json', 'r') as file:
            content = file.read()
        
        expected_content = '[{"id": 1, "width": 10, "height": 5, "x": 0, "y": 0}, {"id": 2, "width": 7, "height": 3, "x": 1, "y": 1}]'
        self.assertEqual(content, expected_content)

        os.remove('Rectangle.json')

""" qn 17"""

class TestBase(unittest.TestCase):
    def test_create_rectangle(self):
        """Test creating a Rectangle instance using the create method"""
        rect_data = {"id": 89, "width": 4, "height": 6, "x": 2, "y": 3}
        rectangle = Rectangle.create(**rect_data)

        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    def test_create_square(self):
        """Test creating a Square instance using the create method"""
        square_data = {"id": 42, "size": 5, "x": 1, "y": 1}
        square = Square.create(**square_data)

        self.assertEqual(square.id, 42)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 1)


if __name__ == "__main__":
    unittest.main()
