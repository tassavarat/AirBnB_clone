#!/usr/bin/python3

"""
Unittest for State
"""

import unittest
from models import storage
from models.base_model import BaseModel


class State_Test(unittest.TestCase):
    """Tests for State class."""

    def setUp(self):
        """Set up tests."""
        storage.reset()


if __name__ == '__main__':
    unittest.main()
