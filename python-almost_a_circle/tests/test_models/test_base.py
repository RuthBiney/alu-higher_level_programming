#!/usr/bin/python3
"""testing the base class"""

import os
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestBase(unittest.TestCase):
    """Test class for base"""

    def test_id(self):
        """Test for id"""
        d1 = Base()
        self.assertEqual(d1.id, 1)
        d2 = Base()
        self.assertEqual(d2.id, 2)
        d3 = Base(89)
        self.assertEqual(d3.id, 89)

    def test_to_json_string(self):
        """test to_json_string"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')
        self.assertEqual(type(Base.to_json_string([{'id': 12}])), str)

    def test_from_json_string(self):
        """test from_json_string"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])
        self.assertEqual(type(Base.from_json_string('[{"id": 12}]')), list)

    def test_save_to_file(self):
        """test save to file"""
        Base._Base__nb_objects = 0

        Square.save_to_file(None)
        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json", "r") as fall:
            self.assertEqual(fall.read(), "[]")

        Square.save_to_file([])
        with open("Square.json", "r") as fall:
            self.assertEqual(fall.read(), "[]")
            self.assertEqual(type(fall.read()), str)

        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as fall:
            self.assertEqual(fall.read(), 
            '[{"id": 1, "size": 1, "x": 0, "y": 0}]')
            Base._Base__nb_objects = 0

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json", "r") as fall:
            self.assertEqual(fall.read(), "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as fall:
            self.assertEqual(fall.read(), "[]")
            self.assertEqual(type(fall.read()), str)

        os.remove("Rectangle.json")
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), 
                             '[{"id": 1, "width": 1, '
                             '"height": 2, "x": 0, "y": 0}]')

if __name__ == '__main__':
    unittest.main()