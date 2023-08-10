#!/usr/bin/python3
import cmd
import sys

"""

This module focuses on creating the command interpreter
using the cmd module

"""

class HBNBCommand(cmd.Cmd):
    """The hbnb class for creating the command interpreter"""
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

