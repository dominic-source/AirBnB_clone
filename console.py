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

    def do_create(self, newModel=None):
        """Creates a new instance of a Model and saves it"""
        if newModel is None:
            print('** class name missing **')
        elif newModel not in HBNBCommand.list_of_models:
            print("** class doesn't exist **")
        else:
            newModel = BaseModel()
            newModel.save()
            print(newModel.id)

    def do_show(self, newModel=None, mid=None):
        """Print the string representation of and instance"""

        if newModel is None:
            print('** class name missing **')
        elif newModel not in HBNBCommand.list_of_models:
            print("** class doesn't exist **")
        elif mid is None:
            print("** instance id missing **")
        else:
            modelid = newModel + '.' + mid
            if modelid not in storage.all():
                print("** no instance found **")
            else:
                value = storage.all()[modelid]
                newInst = BaseModel(value)
                print(newInst)

    def do_destroy(self, nameModel=None, mid=None):
        """This will destroy the class given it name and id"""

        if nameModel is None:
            print('** class name missing **')
        elif nameModel not in HBNBCommand.list_of_models:
            print("** class doesn't exist **")
        elif mid is None:
            print("** instance id missing **")
        else:
            modelid = ".".join([nameModel, mid])
            if modelid not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[modelid]
                storage.save()
                

    def do_all(self, nameModel=None):
        """
        Prints all string representation of all the
        instances based or not on the class name
        
        """
        printout = []

        if nameModel is None or len(nameModel) == 0:
            value = storage.all().copy()
            if len(value) > 0:
                for key, evalue in value.items():
                    newInst = BaseModel(evalue)
                    printout.append(newInst.__str__())
        else:
            if nameModel not in HBNBCommand.list_of_models:
                print("** class doesn't exist **")
            else:
                value = storage.all().copy()
                for key, evalue in value.items():
                    if nameModel == key.split('.')[0]:
                        newInst = BaseModel(evalue)
                        printout.append(newInst.__str__())
        
        if len(printout) != 0:
            print(printout)

    def do_update(self, *args):
        """Updates an instance base on the class name and id"""
        
        if args is None:
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
            value = store[nameModelId][args[2]]
            try:
                if isinstance(value, str):
                    store[nameModelId][args[2]] = str(args[3])
                elif isinstance(value, int):
                    store[nameModelId][args[2]] = int(args[3])
                elif isinstance(value, float):
                    store[nameModelId][args[2]] = float(args[3])
            except ValueError:
                pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

