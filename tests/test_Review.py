#!/usr/bin/python3

"""
Unittest for Review
"""

import unittest
from models import storage
from models.base_model import BaseModel


class Review_Test(unittest.TestCase):
    """Tests for Review class."""

    def setUp(self):
        """Set up tests."""
        storage.reset()


if __name__ == '__main__':
    unittest.main()

