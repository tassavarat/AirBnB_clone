#!/usr/bin/python3

"""
Unittest for City
"""

import unittest
from models import storage
from models.base_model import BaseModel


class City_Test(unittest.TestCase):
    """Tests for City class."""

    def setUp(self):
        """Set up tests."""
        storage.reset()


if __name__ == '__main__':
    unittest.main()
