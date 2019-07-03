#!/usr/bin/python3

"""
Unittest for the Console class
"""

import unittest
import sys
from unittest.mock import patch
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from console import HBNBCommand
from io import StringIO


class Console_Test(unittest.TestCase):
    """Tests for the console."""

    def setUp(self):
        """Set up tests."""
        storage.reset()

    def test_02_quit(self):
        """Test to validate quit works."""
        with patch("sys.stdout", new=StringIO()) as o:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_04_help(self):
        """Test to validate help works."""
        output = "\nDocumented commands (type help <topic>):\n"\
            + "========================================\n"\
            + "EOF  all  count  create  destroy  help  quit  show  update\n\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("help")
            self.assertEqual(output, o.getvalue())

    def test_08_all(self):
        """Test to validate all works."""
        b = BaseModel()
        s = State()
        u = User()
        a = Amenity()
        r = Review()
        c = City()
        p = Place()
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("BaseModel.all()")
            self.assertIn('BaseModel', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("State.all()")
            self.assertIn('State', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("User.all()")
            self.assertIn('User', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Amenity.all()")
            self.assertIn('Amenity', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Review.all()")
            self.assertIn('Review', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("City.all()")
            self.assertIn('City', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Place.all()")
            self.assertIn('Place', o.getvalue())

    def test_09_count(self):
        """Test if count works"""
        b = BaseModel()
        s = State()
        u = User()
        a = Amenity()
        r = Review()
        c = City()
        p = Place()
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual('1\n', o.getvalue())
        b2 = BaseModel()
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual('2\n', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual('1\n', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual('1\n', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual('1\n', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual('1\n', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual('1\n', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual('1\n', o.getvalue())

    def test_10_update(self):
        """Test to validate update works."""
        b = BaseModel()
        b_id = b.id
        s = State()
        s_id = s.id
        u = User()
        u_id = u.id
        a = Amenity()
        a_id = a.id
        r = Review()
        r_id = r.id
        c = City()
        c_id = c.id
        p = Place()
        p_id = p.id
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('BaseModel.update(' +
                                 b_id + ' "first_name", "John")')
            self.assertTrue(hasattr(b, 'first_name'))
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('State.update(' +
                                 s_id + ' "first_name", "John")')
            self.assertTrue(hasattr(s, 'first_name'))
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('User.update(' +
                                 u_id + ' "first_name", "John")')
            self.assertTrue(hasattr(u, 'first_name'))
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('Amenity.update(' +
                                 a_id + ' "first_name", "John")')
            self.assertTrue(hasattr(a, 'first_name'))
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('Review.update(' +
                                 r_id + ' "first_name", "John")')
            self.assertTrue(hasattr(r, 'first_name'))
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('City.update(' +
                                 c_id + ' "first_name", "John")')
            self.assertTrue(hasattr(c, 'first_name'))
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('Place.update(' +
                                 p_id + ' "first_name", "John")')
            self.assertTrue(hasattr(p, 'first_name'))


if __name__ == '__main__':
    unittest.main()
