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
        b = Base()
        self.assertIsInstance(b, Base)
    def test_create_instance_with_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)
    def test_auto_assign_id_without_passing_id(self):
        b = Base()
        self.assertEqual(b.id, 1)
    def test_auto_assign_id_increments(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

"""quetion 15"""

    def test_to_json_string_with_none(self):
        """Test JSON string conversion when input is None"""        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_with_empty_list(self):
         """Test JSON string conversion when input is an empty list"""
         self.assertEqual(Base.to_json_string([]), "[]")

     def test_to_json_string_with_list_of_dicts(self):
         """Test JSON string conversion with valid dictionaries"""

          list_dicts = [{"id": 1, "width": 10, "height": 5}]
          json_str = Base.to_json_string(list_dicts)
          expected_str = '[{"id": 1}, {"id": 2, "width": 4}]'
          self.assertEqual(json_str, expected_str)

""" 16"""

     def test_save_to_file(self):
        """Test saving Rectangle instances to a file"""
        rectangle = Rectangle(10, 5, 0, 0)
        rectangle2 = Rectangle(7, 3, 1, 1)
        
        Base.save_to_file([rectangle, rectangle2])
        
        with open('Rectangle.json', 'r') as file:
            content = file.read()
        
        expected_content = '[{"id": 1, "width": 10, "height": 5, "x": 0, "y": 0}, {"id": 2, "width": 7, "height": 3, "x": 1, "y": 1}]'
        self.assertEqual(content, expected_content)

        os.remove('Rectangle.json')

if __name__ == "__main__":
    unittest.main()
