#!/usr/bin/python3

"""
Unittest for BaseModel
"""

import unittest
import os
import re
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
        self.assertEqual(hasattr(b, "id"), True)
        self.assertEqual(hasattr(b, "created_at"), True)
        self.assertEqual(hasattr(b, "updated_at"), True)

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
        self.assertEqual(hasattr(b, "string"), True)
        self.assertEqual(hasattr(b, "number"), True)
        self.assertEqual(hasattr(b, "list"), True)
        self.assertEqual(hasattr(b, "dict"), True)
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


if __name__ == '__main__':
    unittest.main()
