#!/usr/bin/python3

"""
Unittest for BaseModel
"""

import unittest
import os
import re
from time import sleep
from models.base_model import BaseModel


class BaseModel_Test(unittest.TestCase):
    """Tests for base class."""

    def setUp(self):
        """Set up tests."""
        pass

    def test_00_class_type(self):
        """Test for correct class type."""
        b = BaseModel()
        self.assertEqual(b.__class__.__name__, "BaseModel")

    def test_01_no_args(self):
        """Test for no arguments passed into BaseModel."""
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_02_correct_types_in_args(self):
        """Test for correct types in args."""
        b = BaseModel()
        self.assertEqual(type(b.id), str)
        self.assertEqual(b.created_at.__class__.__name__, "datetime")
        self.assertEqual(b.updated_at.__class__.__name__, "datetime")

    def test_03_adding_extra_parameters(self):
        """Test for manually adding parameters to empty BaseModel."""
        b = BaseModel()
        b.string = "Tu"
        b.number = 1106
        b.list = [1, 2, 3]
        b.dict = {"a": 1}
        self.assertTrue(hasattr(b, "string"))
        self.assertTrue(hasattr(b, "number"))
        self.assertTrue(hasattr(b, "list"))
        self.assertTrue(hasattr(b, "dict"))
        self.assertEqual(type(b.string), str)
        self.assertEqual(type(b.number), int)
        self.assertEqual(type(b.list), list)
        self.assertEqual(type(b.dict), dict)

    def test_04_str(self):
        """Test to validate __str__ method is working properly"""
        b = BaseModel()
        p = r'(^\[BaseModel]) (\(\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\)) (\{.*}$)'
        prog = re.compile(p)
        match = prog.match(str(b))
        self.assertTrue(match is not None)

    def test_05_save(self):
        """Test to validate that updated_at is changed when saved."""
        b = BaseModel()
        first_time = b.updated_at
        sleep(.5)
        b.save()
        second_time = b.updated_at
        self.assertNotEqual(first_time, second_time)

    def test_06_to_dict(self):
        """Test to validate to_dict is outputting correctly."""
        b = BaseModel()
        b.name = "Tu"
        b.number = 1987
        d = b.to_dict()
        self.assertTrue('number' in d)
        self.assertTrue('name' in d)
        self.assertTrue('id' in d)
        self.assertTrue('created_at' in d)
        self.assertTrue('updated_at' in d)
        self.assertTrue('__class__' in d)

    def test_06_to_dict_values(self):
        """Test to validate to_dict values are all strings."""
        b = BaseModel()
        b.name = "Tu"
        b.number = 1987
        d = b.to_dict()
        self.assertEqual(type(d['name']), str)
        self.assertEqual(type(d['number']), int)
        self.assertEqual(type(d['created_at']), str)
        self.assertEqual(type(d['updated_at']), str)
        self.assertEqual(type(d['id']), str)
        self.assertEqual(type(d['__class__']), str)

    def test_07_recreate_instance(self):
        """Test to create instances from to_dict."""
        b = BaseModel()
        b.name = "Tim"
        b.number = 1992
        d = b.to_dict()
        new_b = BaseModel(**d)
        self.assertEqual(b.id, new_b.id)
        self.assertEqual(b.created_at, new_b.created_at)
        self.assertEqual(b.updated_at, new_b.updated_at)
        self.assertEqual(b.name, new_b.name)
        self.assertEqual(b.number, new_b.number)
        self.assertEqual(type(new_b.id), str)
        self.assertEqual(new_b.created_at.__class__.__name__, "datetime")
        self.assertEqual(new_b.updated_at.__class__.__name__, "datetime")
        self.assertTrue(b is not new_b)

    def test_08_empty_dict(self):
        """Test for empty dict as an arg."""
        d = {}
        b = BaseModel(**d)
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_09_None(self):
        """Test for None as an arg."""
        b = BaseModel(None)
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))
"""
    def test_10_manual_kwargs(self):
        Test for manually entering in kwargs.
        with self.assertRaises(TypeError):
            b = BaseModel()
"""

if __name__ == '__main__':
    unittest.main()
