#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
import models


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "
    valid_models = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                    "Review"]
    valid_cmds = ["all", "count", "show", "destroy", "update"]

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
        """Ensures that previous command is not run twice"""

    def do_create(self, cls):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        if not cls:
            print("** class name missing **")
            return
        try:
            new_class = eval(cls)()
            print(new_class.id)
            new_class.save()
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on the class
        name and id
        """
        params = args.split()
        if len(params) == 0:
            print("** class name missing **")
        elif len(params) == 1:
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
        params = args.split()
        if len(params) == 0:
            print("** class name missing **")
        elif len(params) == 1:
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
        """Prints all string representation of all instances based or not on
        the class name
        """
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
        """Updates an instance based on the class name and id by adding or up
        dating attribute
        """
        params = args.split()
        if len(params) == 0:
            print("** class name missing **")
        elif len(params) == 1:
            print("** instance id missing **")
        elif len(params) == 2:
            print("** attribute name missing **")
        elif len(params) == 3:
            print("** value missing **")
        elif params[0] not in HBNBCommand.valid_models:
            print("** class doesn't exist **")
        else:
            try:
                if params[3].isdigit():
                    params[3] = int(params[3])
                elif float(params[3]):
                    params[3] = float(params[3])
            except ValueError:
                pass
            k = params[0] + '.' + params[1]
            if k in models.storage.all():
                setattr(models.storage.all()[k], params[2],
                        params[3])
                models.storage.save()
            else:
                print("** no instance found **")

    def do_count(self, args):
        """Retrieves the number of instances of a class."""
        params = args.split()
        if len(params) == 0:
            print("** class name missing **")
        print(len([k for k in models.storage.all().keys()
              if k.split('.')[0] == params[0]]))

    def default(self, inp):
        """Converts custom user input into commands"""
        if '.' not in inp:
            print("** invalid input **")
            return
        cls_name = inp.split('.')[0]
        if cls_name not in HBNBCommand.valid_models:
            print("** class doesn't exist **")
            return
        cmd = inp.split('.')[1]
        if '(' not in cmd and ')' not in cmd:
            print("** invalid input **")
            return
        cmd_left = cmd.split('(')[0]
        cmd_right = cmd.split('(')[-1][:-1]
        if cmd_left not in HBNBCommand.valid_cmds:
            print("** invalid command **")
            return
        if cmd_left == "all":
            return self.do_all(cls_name)
        if cmd_left == "count":
            return self.do_count(cls_name)
        if cmd_left == "show":
            return self.do_show(cls_name + " " + cmd_right)
        if cmd_left == "destroy":
            return self.do_destroy(cls_name + " " + cmd_right)
        if cmd_left == "update":
            if '{' in cmd_right and '}':
                index = cmd_right.index(',')
                cls_id = cmd_right[:index].replace("\"", "")
                string_d = cmd_right[index + 1:]
                d = eval(string_d)
                for k, v in d.items():
                    arg = ""
                    arg += cls_name + " " + cls_id + " " + k + " " + str(v)
                    self.do_update(arg)
            else:
                arg = ""
                arg += cls_name + " "
                for i in cmd_right.split(', '):
                    arg += i.replace("\"", "") + " "
                return self.do_update(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
