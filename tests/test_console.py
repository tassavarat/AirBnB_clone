#!/usr/bin/python3

"""
Unittest for the console class
"""

import unittest
import sys
import re
from unittest.mock import create_autospec
from models import storage
from models.base_model import BaseModel
from console import HBNBCommand
from io import StringIO


class Console_Test(unittest.TestCase):
    """Tests for the console."""

    def setUp(self):
        """Set up tests."""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdin)
        storage.reset()

    def create(self, server=None):
        """Create a test environment."""
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def _last_write(self, nr=None):
        """:return: last `n` output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0],
                       self.mock_stdout.write.call_args_list[-nr:]))

    def test_00_interactive_mode(self):
        """Test to validate the console works in interactive mode."""
        pass

    def test_01_non_interactive_mode(self):
        """Test to validate the console works in non-interactive mode."""
        pass

    def test_02_quit(self):
        """Test to validate quit works."""
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))

    def test_03_EOF(self):
        """Test to validate EOF works."""
        pass

    def test_04_help(self):
        """Test to validate help works."""
        cli = self.create()
        cli.onecmd("help")
        output = "\nDocumented commands (type help <topic>):\n"\
            + "========================================\n"\
            + "EOF  all  count  create  destroy  help  quit  show  update\n\n"
        self.assertEqual(output, self._last_write(5))

    def test_04a_help_EOF(self):
        """Test to validate help EOF works."""
        cli = self.create()
        cli.onecmd("help EOF")
        output = "Quit command to exit the program\n"
        self.assertEqual(output, self._last_write(1))

    def test_04b_help_quit(self):
        """Test to validate help quit works."""
        cli = self.create()
        cli.onecmd("help quit")
        output = "Quit command to exit the program\n"
        self.assertEqual(output, self._last_write(2))

    def test_04c_help_all(self):
        """Test to validate help all works."""
        cli = self.create()
        cli.onecmd("help all")
        output = "Prints all str repr of all instances of class name\n"
        self.assertEqual(output, self._last_write(2))

    def test_04d_help_count(self):
        """Test to validate help count works."""
        cli = self.create()
        cli.onecmd("help count")
        output = "Retrieves the number of instances of a class\n"
        self.assertEqual(output, self._last_write(1))

    def test_04e_help_create(self):
        """Test to validate help create works."""
        cli = self.create()
        cli.onecmd("help create")
        output = "Creates a new instance, saves it, and prints id\n"
        self.assertEqual(output, self._last_write(1))

    def test_04f_help_destroy(self):
        """Test to validate help destroy works."""
        cli = self.create()
        cli.onecmd("help destroy")
        output = "Deletes an instance based on the class name and id\n"
        self.assertEqual(output, self._last_write(1))

    def test_04g_help_show(self):
        """Test to validate help show works."""
        cli = self.create()
        cli.onecmd("help show")
        o = "Prints the str repr of an instance with class name and id\n"
        self.assertEqual(o, self._last_write(1))

    def test_04h_help_update(self):
        """Test to validate help update works."""
        cli = self.create()
        cli.onecmd("help update")
        o = "Updates an instance based on the class name and id\n"
        self.assertEqual(o, self._last_write(1))

    def test_05_create(self):
        """Test to validate create works."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("create BaseModel")
        p = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
        prog = re.compile(p)
        self.assertNotEqual(None, prog.match(output.getvalue()))
        sys.stdout = sys.__stdout__

    def test_05a_create_bad_value(self):
        """Test to validate create with bad value."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("create Monster")
        self.assertEqual("** class doesn't exist **\n", output.getvalue())
        sys.stdout = sys.__stdout__

    def test_05b_create_empty_value(self):
        """Test to validate create with bad empty."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("create")
        self.assertEqual("** class name missing **\n", output.getvalue())
        sys.stdout = sys.__stdout__

    def test_05c_create_extra_values(self):
        """Test to validate create with extra empty."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("create BaseModel hello")
        p = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
        prog = re.compile(p)
        self.assertNotEqual(None, prog.match(output.getvalue()))
        sys.stdout = sys.__stdout__

    def test_06a_show(self):
        """Test to validate show works."""
        cli = self.create()
        b = BaseModel()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("show BaseModel " + b.id)
        self.assertTrue(output.getvalue().startswith('[BaseModel]'))
        sys.stdout = sys.__stdout__

    def test_06b_show_missing_class(self):
        """Test for show with missing class."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("show ")
        self.assertEqual("** class name missing **\n", output.getvalue())
        sys.stdout = sys.__stdout__

    def test_06b_show_missing_class(self):
        """Test for show with missing class."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("show ")
        self.assertEqual("** class name missing **\n", output.getvalue())
        sys.stdout = sys.__stdout__

    def test_06c_show_missing_id(self):
        """Test for show with missing id."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("show MyModel")
        self.assertEqual("** class doesn't exist **\n", output.getvalue())
        sys.stdout = sys.__stdout__

    def test_06d_show_missing_class(self):
        """Test for show with missing class."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("show BaseModel")
        self.assertEqual("** instance id missing **\n", output.getvalue())
        sys.stdout = sys.__stdout__

    def test_06e_show_missing_class(self):
        """Test for show with missing class."""
        cli = self.create()
        output = StringIO()
        sys.stdout = output
        cli.onecmd("show BaseModel 32432423")
        self.assertEqual("** no instance found **\n", output.getvalue())
        sys.stdout = sys.__stdout__

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
