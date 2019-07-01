#!/usr/bin/python3

"""
Unittest for the console
"""

import unittest
from models import storage
from models.base_model import BaseModel


class Console_Test(unittest.TestCase):
    """Tests for the console."""

    def setUp(self):
        """Set up tests."""
        pass

    def test_00_interactive_mode(self):
        """Test to validate the console works in interactive mode."""
        pass

    def test_01_non_interactive_mode(self):
        """Test to validate the console works in non-interactive mode."""
        pass

    def test_02_quit(self):
        """Test to validate quit works."""
        pass

    def test_03_EOF(self):
        """Test to validate EOF works."""
        pass

    def test_04_help(self):
        """Test to validate help works."""
        pass

    def test_05_create(self):
        """Test to validate create works."""
        pass

    def test_06_show(self):
        """Test to validate show works."""
        pass

    def test_07_destroy(self):
        """Test to validate destroy works."""
        pass

    def test_08_all(self):
        """Test to validate all works."""
        pass

    def test_09_update(self):
        """Test to validate update works."""
        pass


if __name__ == '__main__':
    unittest.main()
