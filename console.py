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
                print(e.__class__.__name__)
                print("** class doesn't exist **")

    def do_destroy(self, args=None):
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
                # print(e.__class__.__name__)
                print("** class doesn't exist **")

    def do_all(self, cls_name=None):
        valid_models = ["BaseModel"]
        params = cls_name.split()
        str_list = []
        if len(params) == 0:
            for v in models.storage.all().values():
                str_list.append(str(v))
        else:
            if cls_name not in valid_models:
                print("** class doesn't exist **")
                return
            for k, v in models.storage.all().items():
                left = k.split('.')[0]
                if left == cls_name:
                    str_list.append(str(v))
        print(str_list)

    def do_update(self, args=None):
        valid_models = ["BaseModel"]
        params = args.split()
        if len(params) == 0:
            print("** class name missing **")
        elif len(params) == 1:
            print("** instance id missing **")
        elif len(params) == 2:
            print("** attribute name missing **")
        elif len(params) == 3:
            print("* value missing **")
        elif params[0] not in valid_models:
            print("** class doesn't exist **")
        else:
            try:
                if params[3].isdigit():
                    params[3] = int(params[3])
                elif float(params[3]):
                    params[3] = float(params[3])
            except ValueError:
                pass
            for k, v in models.storage.all().items():
                left = k.split('.')[0]
                right = k.split('.')[1]
                if left == params[0] and right == params[1]:
                    setattr(v, params[2], params[3])
                    models.storage.save()
                else:
                    print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
