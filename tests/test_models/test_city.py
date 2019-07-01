#!/usr/bin/python3

"""
Unittest for City
"""

import unittest
import re
from time import sleep
from models import storage
from models.city import City


class City_Test(unittest.TestCase):
    """Tests for City class."""

    def setUp(self):
        """Set up tests."""
        storage.reset()

    def test_00_valid_user(self):
        """Test to validate a user."""
        u = City()
        self.assertEqual(u.__class__.__name__, "City")

    def test_01_no_args(self):
        """Test for no arguments passed into City"""
        u = City()
        self.assertTrue(hasattr(u, "id"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))
        self.assertTrue(hasattr(u, "name"))
        self.assertTrue(hasattr(u, "state_id"))

    def test_02_correct_types_in_args(self):
        """Test for correct types in args"""
        u = City()
        self.assertEqual(type(u.id), str)
        self.assertEqual(type(u.name), str)
        self.assertEqual(type(u.state_id), str)
        self.assertEqual(u.created_at.__class__.__name__, "datetime")
        self.assertEqual(u.updated_at.__class__.__name__, "datetime")

    def test_03_adding_extra_parameters(self):
        """Test for manually adding parameters to empty BaseModel"""
        u = City()
        u.string = "Tu"
        u.number = 1106
        u.list = [1, 2, 3]
        u.dict = {"a": 1}
        self.assertTrue(hasattr(u, "string"))
        self.assertTrue(hasattr(u, "number"))
        self.assertTrue(hasattr(u, "list"))
        self.assertTrue(hasattr(u, "dict"))
        self.assertEqual(type(u.string), str)
        self.assertEqual(type(u.number), int)
        self.assertEqual(type(u.list), list)
        self.assertEqual(type(u.dict), dict)

    def test_04_str(self):
        """Test to validate __str__ method is working properly"""
        u = City()
        p = r'(^\[City]) (\(\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\)) (\{.*}$)'
        prog = re.compile(p)
        match = prog.match(str(u))
        self.assertTrue(match is not None)

    def test_05_save(self):
        """Test to validate that updated_at is changed when saved"""
        u = City()
        first_time = u.updated_at
        sleep(.5)
        u.save()
        second_time = u.updated_at
        self.assertNotEqual(first_time, second_time)

    def test_06_to_dict(self):
        """Test to validate to_dict is outputting correctly"""
        u = City()
        u.name = "Tu"
        u.number = 1987
        d = u.to_dict()
        self.assertTrue('number' in d)
        self.assertTrue('name' in d)
        self.assertTrue('id' in d)
        self.assertTrue('created_at' in d)
        self.assertTrue('updated_at' in d)
        self.assertTrue('__class__' in d)

    def test_06a_to_dict_values(self):
        """Test to validate to_dict values are all strings"""
        u = City()
        u.name = "Tu"
        u.number = 1987
        d = u.to_dict()
        self.assertEqual(type(d['name']), str)
        self.assertEqual(type(d['number']), int)
        self.assertEqual(type(d['created_at']), str)
        self.assertEqual(type(d['updated_at']), str)
        self.assertEqual(type(d['id']), str)
        self.assertEqual(type(d['__class__']), str)

    def test_07_recreate_instance(self):
        """Test to create instances from to_dict"""
        u = City()
        u.name = "Tim"
        u.number = 1993
        d = u.to_dict()
        new_u = City(**d)
        self.assertEqual(u.id, new_u.id)
        self.assertEqual(u.created_at, new_u.created_at)
        self.assertEqual(u.updated_at, new_u.updated_at)
        self.assertEqual(u.name, new_u.name)
        self.assertEqual(u.number, new_u.number)
        self.assertEqual(type(new_u.id), str)
        self.assertEqual(new_u.created_at.__class__.__name__, "datetime")


if __name__ == '__main__':
    unittest.main()
