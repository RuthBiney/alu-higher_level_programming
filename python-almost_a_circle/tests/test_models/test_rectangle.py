#!/usr/bin/python3
"""Test for rectangle file"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch
import os 

class TestRectangle(unittest.TestCase):
    """Test for rectangle calss"""

    def startUp(self):
        """Test for Start up"""
        Base._Base__nb_objects = 0
        l1 = Rectangle(1, 2)
        l2 = Rectangle(1, 2, 3)
        l3 = Rectangle(1, 2,3 ,4)
        l4 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(l4.id, 5)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r5 = Rectangle(0, 2)
        
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r6 = Rectangle(1, 0)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r7 = Rectangle(-1, 2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r8 = Rectangle(1, -2)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r9 = Rectangle(1, 2, -3)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r10 = Rectangle(1, 2, 3, -4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r11 = Rectangle("1", 2)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r12 = Rectangle(1, "2")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r13 = Rectangle(1, 2, "3")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r14 = Rectangle(1, 2, 3, "4")

    def test_area(self):
            """Test for Area"""
            a = Rectangle(4, 2)
            self.assertEqual(a.area(), 8)

    def test_str_(self):
            """Test for __str__"""
            Base._Base__nb_objects = 0
            s = Rectangle(4, 2)
            with patch('sys.stdout', n=StringIO()) as fall:
                print(s)
                self.assertEqual(fall.getvalue(), "[Rectangle] (1) 0/0 - 10/10")
        
    def test_display(self):
        """Test for display"""
        r1 = Rectangle(4, 2)
        r2 = Rectangle(4, 2, 3)
        r3 = Rectangle(4, 2, 3, 2)
        with patch('sys.stdout', n=StringIO()) as fall:
            r1.display()
            self.assertEqual(fall.getvalue(), (" " * 4 + "#" * 2 + "\n") * 3)
                
        with patch('sys.stdout', n=StringIO()) as f:
             r2.display()
             self.assertEqual(f.getvalue(), "\n" * 8 +
                             (" " * 7 + "#" * 5 + "\n") * 6)
                 
        with patch('sys.stdout', n=StringIO()) as f:
             r3.display()
             self.assertEqual(f.getvalue(), "\n" * 14 +
                             (" " * 13 + "#" * 11 + "\n") * 12)

    def test_dictionary(self):
        """Test for dictionary"""
        Base._Base__nb_objects = 0
        d1 = Rectangle(4, 2)
        self.assertEqual(d1.to_dictionary(),
        {'x': 0, 'y': 0, 'id': 1, 'height': 2, 'width': 4})

    def test_update(self):
        """Test for update"""
        Base._Base__nb_objects = 0
        t1 = Rectangle(4, 2)

        t1.update()
        self.assertEqual(t1.id, 1)

        t1.update(89)
        self.assertEqual(t1.id, 89)

        t1.update(89, 1)
        self.assertEqual(t1.width, 1)
        self.assertEqual(t1.id, 89)

        t1.update(89, 1, 2)
        self.assertEqual(t1.height, 2)
        self.assertEqual(t1.width, 1)
        self.assertEqual(t1.id, 89)

        t1.update(89, 1, 2, 3)
        self.assertEqual(t1.height, 2)
        self.assertEqual(t1.width, 1)
        self.assertEqual(t1.id, 89)
        self.assertEqual(t1.x, 3)

        t1.update(89, 1, 2, 3, 4)
        self.assertEqual(t1.height, 2)
        self.assertEqual(t1.width, 1)
        self.assertEqual(t1.id, 89)
        self.assertEqual(t1.x, 3)
        self.assertEqual(t1.y, 4)

        t1.update(**{'id': 89})
        self.assertEqual(t1.id, 89)

        t1.update(**{'id': 89, 'width': 1})
        self.assertEqual(t1.id, 89)
        self.assertEqual(t1.width, 1)

        t1.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(t1.id, 89)
        self.assertEqual(t1.width, 1)
        self.assertEqual(t1.height, 2)

        t1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(t1.id, 89)
        self.assertEqual(t1.width, 1)
        self.assertEqual(t1.height, 2)
        self.assertEqual(t1.x, 3)

        t1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(t1.id, 89)
        self.assertEqual(t1.width, 1)
        self.assertEqual(t1.height, 2)
        self.assertEqual(t1.x, 3)
        self.assertEqual(t1.y, 4)

    def test_create(self):
        """test for create function"""
        f1 = Rectangle.create(**{'id': 89})
        self.assertEqual(f1.id, 89)

        f1 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(f1.id, 89)
        self.assertEqual(f1.width, 1)

        f1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(f1.id, 89)
        self.assertEqual(f1.width, 1)
        self.assertEqual(f1.height, 2)

        f1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(f1.id, 89)
        self.assertEqual(f1.width, 1)
        self.assertEqual(f1.height, 2)

        f1 = Rectangle.create(**{'id': 89, 'width': 1, 
        'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(f1.id, 89)
        self.assertEqual(f1.width, 1)
        self.assertEqual(f1.height, 2)
        self.assertEqual(f1.x, 3)

    def test_save_to_file(self):
        """Test for save_to_file"""
        Base._Base__nb_objects = 0

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json") as fall:
            self.assertEqual(fall.read(), "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json") as fall:
            self.assertEqual(fall.read(), "[]")
            self.assertEqual(type(f.read()), str)

        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json") as fall:
            self.assertEqual(fall.read(),
                             '[{"id": 1, "width": 1, '
                             '"height": 2, "x": 0, "y": 0}]')

    def test_save_file_empty(self):
        """Test for save_to_file with empty list"""
        Rectangle.save_to_file([])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json") as fall:
            self.assertEqual(fall.read(), "[]")
            self.assertEqual(type(fall.read()), str)

    def test_load_from_file(self):
        """Test for load from file function"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2)])
        file = Rectangle.load_from_file()
        self.assertEqual(type(file), list)
        self.assertEqual(file[0].width, 1)
        self.assertEqual(file[0].height, 2)

if __name__ == '__main__':
    unittest.main()