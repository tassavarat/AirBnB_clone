#!/usr/bin/python3

"""
Unittest for User class
"""

import unittest
from models import storage
from models.base_model import BaseModel


class User_Test(unittest.TestCase):
    """Tests for User class."""

    def setUp(self):
        """Set up tests."""
        storage.reset()


if __name__ == '__main__':
    unittest.main()
