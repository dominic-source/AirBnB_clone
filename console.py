#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.__init__ import storage

"""

This module focuses on creating the command interpreter
using the cmd module

"""

class HBNBCommand(cmd.Cmd):
    """The hbnb class for creating the command interpreter"""
    prompt = '(hbnb) '
    list_of_models = ['BaseModel']

    def do_quit(self, line):
        """The quit command will exit the interpreter"""

        return True

    def do_EOF(self, line):
        """Exit the program when it gets to the End of File"""
        print(line)
        return True

    def emptyline(self):
        """Ensure that when and empty line is entered nothing is executed"""
        pass

    def do_create(self, newModel):
        """Creates a new instance of a Model and saves it"""

        newModel = newModel.split()
        if len(newModel) == 0:
            print('** class name missing **')
        elif newModel[0] not in HBNBCommand.list_of_models:
            print("** class doesn't exist **")
        else:
            if newModel[0] == "BaseModel":
                createModel = BaseModel()
                createModel.save()
            print(createModel.id)

    def do_show(self, args):
        """Print the string representation of and instance"""

        args = args.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.list_of_models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            modelid = args[0] + '.' + args[1]
            if modelid not in storage.all():
                print("** no instance found **")
            else:
                value = storage.all()
                newInst = BaseModel(**(value[modelid]))
                print(newInst)

    def do_destroy(self, args):
        """This will destroy the class given it name and id"""
        args = args.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.list_of_models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            modelid = ".".join([args[0], args[1]])
            if modelid not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[modelid]
                storage.save()

    def do_all(self, nameModel):
        """
        Prints all string representation of all the
        instances based or not on the class name
        """
        printout = []
        nameModel = nameModel.split()
        if len(nameModel) == 0:
            value = storage.all()
            if len(value) > 0:
                for key, evalue in value.items():
                    newInst = BaseModel(**evalue)
                    printout.append(newInst.__str__())
        else:
            if nameModel[0] not in HBNBCommand.list_of_models:
                print("** class doesn't exist **")
            else:
                value = storage.all()
                for key, evalue in value.items():
                    if nameModel[0] == key.split('.')[0]:
                        newInst = BaseModel(**evalue)
                        printout.append(newInst.__str__())

        if len(printout) != 0:
            print(printout)

    @staticmethod
    def merge(args):
        """merge strings together"""


    def do_update(self, args):
        """Updates an instance base on the class name and id"""

        args = args.split()
        print(args)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.list_of_models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif '.'.join([args[0], args[1]]) not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            """Missing attribute name"""
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            nameModelId = '.'.join([args[0], args[1]])
            store = storage.all()
            try:
                value = store[nameModelId][args[2]]
            except ValueError:
                pass
            except KeyError:
                store[nameModelId][args[2]] = args[3]
            else:
                if isinstance(value, str):
                    store[nameModelId][args[2]] = str(args[3])
                elif isinstance(value, int):
                    store[nameModelId][args[2]] = int(args[3])
                elif isinstance(value, float):
                    store[nameModelId][args[2]] = float(args[3])
                else:
                    pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

