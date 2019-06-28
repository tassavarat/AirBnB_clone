#!/usr/bin/python3

"""
Entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        print()
        return True

    def emptyline(self):
        return

    def do_create(self, cls=None):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        if cls is None:
            print("** class name missing **")
            return
        try:
            new_class = eval(cls)()
            print(new_class.id)
            new_class.save()
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args=None):
        """Prints the string representation of an instance based on the class
        name and id
        """
        params = args.split()
        if len(params) == 0:
            print("** class name missing **")
            return
        if len(params) == 1:
            print("** instance id missing **")
            return
        try:
            k = params[0] + '.' + params[1]
            print(models.storage.all()[k])
        except Exception as e:
            print(e.__class__.__name__)
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
