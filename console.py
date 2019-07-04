#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from shlex import split as sp
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "
    valid_models = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                    "Review"]
    valid_cmds = ["all", "count", "show", "destroy", "update"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Ensures that previous command is not run twice"""

    def do_create(self, cls):
        """Creates a new instance, saves it, and prints id"""
        if not cls:
            return(print("** class name missing **"))
        if ' ' in cls:
            cls = cls.split(' ')[0]
        if cls not in HBNBCommand.valid_models:
            print("** class doesn't exist **")
        else:
            new_class = eval(cls)()
            print(new_class.id)
            new_class.save()

    def do_show(self, args):
        """Prints the str repr of an instance with class name and id"""
        params = sp(args)
        if len(params) == 0:
            return(print("** class name missing **"))
        if params[0] not in HBNBCommand.valid_models:
            return(print("** class doesn't exist **"))
        if len(params) == 1:
            print("** instance id missing **")
        else:
            try:
                k = params[0] + '.' + params[1]
                if k in models.storage.all():
                    print(models.storage.all()[k])
                else:
                    print("** no instance found **")
            except Exception as e:
                print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        params = sp(args)
        if len(params) == 0:
            return(print("** class name missing **"))
        if params[0] not in HBNBCommand.valid_models:
            return(print("** class doesn't exist **"))
        if len(params) == 1:
            print("** instance id missing **")
        else:
            try:
                k = params[0] + '.' + params[1]
                if k in models.storage.all():
                    del models.storage.all()[k]
                    models.storage.save()
                else:
                    print("** no instance found **")
            except Exception as e:
                print("** class doesn't exist **")

    def do_all(self, cls_name):
        """Prints all str repr of all instances of class name"""
        str_list = []
        if not cls_name:
            for v in models.storage.all().values():
                str_list.append(str(v))
        else:
            if cls_name not in HBNBCommand.valid_models:
                print("** class doesn't exist **")
                return
            for k, v in models.storage.all().items():
                left = k.split('.')[0]
                if left == cls_name:
                    str_list.append(str(v))
        print(str_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        params = sp(args)
        if len(params) == 0:
            print("** class name missing **")
        elif len(params) == 1:
            print("** instance id missing **")
        elif len(params) > 1:
            k = params[0] + "." + params[1]
            if k not in models.storage.all():
                return(print("** no instance found **"))
        if len(params) == 2:
            print("** attribute name missing **")
        elif len(params) == 3:
            print("** value missing **")
        elif params[0] not in HBNBCommand.valid_models:
            print("** class doesn't exist **")
        else:
            k = params[0] + '.' + params[1]
            val = params[3]
            try:
                if val.isdigit():
                    val = int(val)
                elif float(val):
                    val = float(val)
            except ValueError:
                pass
            if k in models.storage.all():
                setattr(models.storage.all()[k], params[2], params[3])
            else:
                return(print("** no instance found **"))

    def do_count(self, args):
        """Retrieves the number of instances of a class"""
        params = args.split()
        if len(params) == 0:
            print("** class name missing **")
        print(len([k for k in models.storage.all().keys()
              if k.split('.')[0] == params[0]]))

    def default(self, inp):
        """Converts custom user input into commands"""
        parsed_inp = self.default_error_check(inp)
        if not parsed_inp:
            return
        cls_name, cmd, args = parsed_inp
        if cmd == "all":
            return self.do_all(cls_name)
        if cmd == "count":
            return self.do_count(cls_name)
        if cmd == "show":
            return self.do_show(cls_name + " " + args)
        if cmd == "destroy":
            return self.do_destroy(cls_name + " " + args)
        if cmd == "update":
            if '{' in args and '}' in args:
                self.evaluate_kwargs(cls_name, args)
            else:
                self.evaluate_args(cls_name, args)

    def default_error_check(self, inp):
        """Checks for errors in input for default."""
        if '.' not in inp:
            return(print("** invalid input **"))
        cls_name = inp.split('.')[0]
        if cls_name not in HBNBCommand.valid_models:
            return(print("** class doesn't exist **"))
        idx = inp.index('.')
        cmd = inp[idx + 1:]
        if '(' not in cmd and ')' not in cmd:
            return(print("** invalid input **"))
        cmd_left = cmd.split('(')[0]
        cmd_right = cmd.split('(')[-1][:-1]
        if cmd_left not in HBNBCommand.valid_cmds:
            return(print("** invalid command **"))
        return [cls_name, cmd_left, cmd_right]

    def evaluate_kwargs(self, cls_name, cmd):
        """Converts string to correct format for update method."""
        idx = cmd.index(',')
        cls_id = cmd[:idx].replace("\"", "")
        string_d = cmd[idx + 1:]
        d = eval(string_d)
        for k, v in d.items():
            arg = cls_name + " " + cls_id + " " + k + " " + '"' +\
                    str(v) + '"'
            self.do_update(arg)

    def evaluate_args(self, cls_name, cmd):
        """Converts string to correct format for update method."""
        arg = cls_name + " "
        for i in cmd.split(', ')[:-1]:
            arg += i.replace("\"", "") + " "
        arg += cmd.split(', ')[-1]
        self.do_update(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
