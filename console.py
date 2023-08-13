#!/usr/bin/python3
"""

This module focuses on creating the command interpreter
using the cmd module

"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """The hbnb class for creating the command interpreter"""

    prompt = '(hbnb) '
    listModels = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                  'State': State, 'City': City, 'Amenity': Amenity,
                  'Review': Review}

    def default(self, line):
        """Handle other commands that were not directly created"""

        task = line.split('.')
        try:
            if task[1].endswith(')') and '(' in task[1]:
                attr_sidx = task[1].index('(')
                attr_eidx = task[1].index(')')
                argument = ' '.join([task[0], task[1][attr_sidx+1:attr_eidx]])
                command = task[1][:attr_sidx]
                if '{' not in task[1]:
                    argument = ''.join(argument.split(','))
                    attr = "do_{}".format(command)
                    if hasattr(self, attr):
                        method_me = getattr(self, attr)
                        method_me(argument)
                    elif attr == "do_count":
                        value = storage.all()
                        count = 0
                        for key, evalue in value.items():
                            if task[0] == key.split('.')[0]:
                                count += 1
                            print(count)
                    else:
                        print(f"*** Unknown syntax: {command}")
                elif '{' in task[1]:
                    curlyStart = argument.index('{')
                    curlyEnd = argument.index('}')
                    mydict = argument[curlyStart+1:curlyEnd]
                    arr = mydict.split(',')
                    id = argument.split(',')[0].split(' ')[1]
                    for i in arr:
                        method_me = getattr(self, "do_{}".format(command))
                        kjSplit = i.split(':')
                        key = kjSplit[0].strip()
                        value = kjSplit[1].strip()
                        if key.startswith('\'') and key.endswith('\''):
                            key = key[1:-1]
                        if value.startswith('\'') and value.endswith('\''):
                            value = value[1:-1]
                        keyvalue = ' '.join([key, value])
                        args = task[0] + ' ' + id + ' ' + keyvalue
                        method_me(args)
            else:
                print(f"*** Unknown syntax: {line}")
        except IndexError:
            print(f"*** Unknown syntax: {line}")

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

        newModel = self.splitmodify(newModel)
        if len(newModel) == 0:
            print('** class name missing **')
        elif newModel[0] not in HBNBCommand.listModels:
            print("** class doesn't exist **")
        else:
            createModel = HBNBCommand.listModels[newModel[0]]()
            createModel.save()
            print(createModel.id)

    def do_show(self, args):
        """Print the string representation of and instance"""

        args = self.splitmodify(args)
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.listModels:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            modelid = args[0] + '.' + args[1]
            if modelid not in storage.all():
                print("** no instance found **")
            else:
                value = storage.all()
                newInst = value[modelid]
                print(newInst)

    def do_destroy(self, args):
        """This will destroy the class given it name and id"""
        args = self.splitmodify(args)
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.listModels:
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
        nameModel = self.splitmodify(nameModel)
        if len(nameModel) == 0:
            value = storage.all()
            if len(value) > 0:
                for key, evalue in value.items():
                    printout.append(evalue.__str__())
        else:
            if nameModel[0] not in HBNBCommand.listModels:
                print("** class doesn't exist **")
            else:
                value = storage.all()
                for key, evalue in value.items():
                    if nameModel[0] == key.split('.')[0]:
                        printout.append(evalue.__str__())

        if len(printout) != 0:
            print(printout)

    def splitmodify(self, args):
        """merge strings together and return and array of strings"""
        start = 0
        newArr = []
        if ("\'" not in args) and ("\"" not in args):
            return args.split()
        else:
            values = args.split()
            while (start < len(values)):
                if values[start].startswith('\"'):
                    for i in range(start, len(values)):
                        if values[i].endswith('\"'):
                            newArr.append(' '.join(values[start:i+1])[1:-1])
                            break
                        elif i == (len(values) - 1):
                            if not (values[i].endswith('\"')):
                                newArr.append(' '.join(values[start:i+1])[1:])
                    start = i
                elif values[start].endswith('\"'):
                    newArr.append(values[start][:-1])
                else:
                    newArr.append(values[start])
                start += 1
        return newArr

    def do_update(self, args):
        """Updates an instance base on the class name and id"""

        args = self.splitmodify(args)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.listModels:
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
                value = store[nameModelId].__dict__[args[2]]
            except KeyError:
                store[nameModelId].__dict__[args[2]] = args[3]
                store[nameModelId].save()
            except ValueError:
                pass
            else:
                if isinstance(value, str):
                    store[nameModelId].__dict__[args[2]] = str(args[3])
                    store[nameModelId].save()
                elif isinstance(value, int):
                    try:
                        store[nameModelId].__dict__[args[2]] = int(args[3])
                    except ValueError:
                        pass
                    else:
                        store[nameModelId].save()
                    try:
                        store[nameModelId].__dict__[args[2]] = float(args[3])
                    except ValueError:
                        pass
                    else:
                        store[nameModelId].save()
                else:
                    pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
