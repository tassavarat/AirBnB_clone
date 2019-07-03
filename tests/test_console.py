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

    def test_01_quit(self):
        """Test to validate quit works."""
        with patch("sys.stdout", new=StringIO()) as o:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_02_help(self):
        """Test to validate help works."""
        output = "\nDocumented commands (type help <topic>):\n"\
            + "========================================\n"\
            + "EOF  all  count  create  destroy  help  quit  show  update\n\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("help")
            self.assertEqual(output, o.getvalue())
        output = "Quit command to exit the program\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(output, o.getvalue())
        output = "Retrieves the number of instances of a class\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("help count")
            self.assertEqual(output, o.getvalue())
        output = "Creates a new instance, saves it, and prints id\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("help create")
            self.assertEqual(output, o.getvalue())
        output = "Deletes an instance based on the class name and id\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(output, o.getvalue())
        output = "Quit command to exit the program\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(output, o.getvalue())
        output = "Prints the str repr of an instance with class name and id\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("help show")
            self.assertEqual(output, o.getvalue())
        output = "Updates an instance based on the class name and id\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("help update")
            self.assertEqual(output, o.getvalue())

    def test_03_destroy_errors(self):
        """Test to validate destroy errors."""
        output = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("MyModel.destroy()")
            self.assertEqual(output, o.getvalue())
        output = "** instance id missing **\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("BaseModel.destroy()")
            self.assertEqual(output, o.getvalue())
        output = "** no instance found **\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('BaseModel.destroy("holberton")')
            self.assertEqual(output, o.getvalue())

    def test_04_destroy(self):
        """Test to validate destroy works."""
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
            HBNBCommand().onecmd("BaseModel.destroy(" + b_id + ")")
            HBNBCommand().onecmd("BaseModel.show(" + b_id + ")")
            self.assertNotIn('BaseModel', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("State.destroy(" + s_id + ")")
            HBNBCommand().onecmd("State.show(" + s_id + ")")
            self.assertNotIn('State', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("User.destroy(" + u_id + ")")
            HBNBCommand().onecmd("User.show(" + s_id + ")")
            self.assertNotIn('User', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Amenity.destroy(" + a_id + ")")
            HBNBCommand().onecmd("Amenity.show(" + a_id + ")")
            self.assertNotIn('Amenity', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Review.destroy(" + r_id + ")")
            HBNBCommand().onecmd("Review.show(" + r_id + ")")
            self.assertNotIn('Review', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("City.destroy(" + c_id + ")")
            HBNBCommand().onecmd("City.show(" + c_id + ")")
            self.assertNotIn('City', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Place.destroy(" + p_id + ")")
            HBNBCommand().onecmd("Place.show(" + p_id + ")")
            self.assertNotIn('Place', o.getvalue())

    def test_05_show_errors(self):
        """Test to validate destroy errors."""
        output = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("MyModel.show()")
            self.assertEqual(output, o.getvalue())
        output = "** instance id missing **\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("BaseModel.show()")
            self.assertEqual(output, o.getvalue())
        output = "** no instance found **\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('BaseModel.show("holberton")')
            self.assertEqual(output, o.getvalue())

    def test_06_show(self):
        """Test to validate show works."""
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
            HBNBCommand().onecmd("BaseModel.show(" + b_id + ")")
            self.assertIn('BaseModel', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("State.show(" + s_id + ")")
            self.assertIn('State', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("User.show(" + u_id + ")")
            self.assertIn('User', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Amenity.show(" + a_id + ")")
            self.assertIn('Amenity', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Review.show(" + r_id + ")")
            self.assertIn('Review', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("City.show(" + c_id + ")")
            self.assertIn('City', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Place.show(" + p_id + ")")
            self.assertIn('Place', o.getvalue())

    def test_07_all(self):
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

    def test_08_count(self):
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
        s1 = State()
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual('2\n', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual('1\n', o.getvalue())
        u1 = User()
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual('2\n', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual('1\n', o.getvalue())
        a1 = Amenity()
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual('2\n', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual('1\n', o.getvalue())
        r1 = Review()
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual('2\n', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual('1\n', o.getvalue())
        c1 = City()
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual('2\n', o.getvalue())
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual('1\n', o.getvalue())
        p1 = Place()
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual('2\n', o.getvalue())

    def test_09_update_errors(self):
        """Test to validate update errors."""
        b = BaseModel()
        b_id = b.id
        output = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("MyModel.update()")
            self.assertEqual(output, o.getvalue())
        output = "** instance id missing **\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("BaseModel.update()")
            self.assertEqual(output, o.getvalue())
        output = "** attribute name missing **\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('BaseModel.update("' + b.id + '")')
            self.assertEqual(output, o.getvalue())
        output = "** value missing **\n"
        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd('BaseModel.update("' +
                                 b.id + '", "first_name")')
            self.assertEqual(output, o.getvalue())

    def test_09_update(self):
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
