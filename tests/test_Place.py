#!/usr/bin/python3

"""
Unittest for Place
"""

import unittest
from models import storage
from models.base_model import BaseModel


class Place_Test(unittest.TestCase):
    """Tests for Place class."""

    def setUp(self):
        """Set up tests."""
        storage.reset()


if __name__ == '__main__':
    unittest.main()
