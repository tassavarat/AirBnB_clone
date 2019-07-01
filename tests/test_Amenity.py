#!/usr/bin/python3

"""
Unittest for Amenity
"""

import unittest
from models import storage
from models.base_model import BaseModel


class Amenity_Test(unittest.TestCase):
    """Tests for Amenity class."""

    def setUp(self):
        """Set up tests."""
        storage.reset()


if __name__ == '__main__':
    unittest.main()
