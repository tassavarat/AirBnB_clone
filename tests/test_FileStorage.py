#!/usr/bin/python3

"""
Unittest for FileStorage
"""

import unittest
import os
from models import storage
from models.base_model import BaseModel


class FileStorage_Test(unittest.TestCase):
    """Tests for File Storge class."""

    def setUp(self):
        """Set up tests."""
        storage.reset()

    def test_00_private_attrs(self):
        """Test to validate attributes are private."""
        with self.assertRaises(AttributeError):
            print(storage.objects)
        with self.assertRaises(AttributeError):
            print(storage.file_path)

    def test_01_all_return_type(self):
        """Test to validate all() returns an object."""
        self.assertEqual(type(storage.all()), dict)

    def test_02_working_save(self):
        """Test to validate save works."""
        b = BaseModel()
        key = "BaseModel" + "." + b.id
        b.save()
        self.assertEqual(storage.all()[key].__class__.__name__, "BaseModel")
        self.assertEqual(storage.all()[key].to_dict(), b.to_dict())

    def test_03_working_reload(self):
        """Test to validate reload works."""
        b = BaseModel()
        key = "BaseModel" + "." + b.id
        b.save()
        b1 = BaseModel()
        key1 = "BaseModel" + "." + b1.id
        b1.save()
        self.assertTrue(storage.all()[key] is not None)
        self.assertTrue(storage.all()[key1] is not None)
        with self.assertRaises(KeyError):
            self.assertTrue(storage.all()[12345] is None)


if __name__ == '__main__':
    unittest.main()
