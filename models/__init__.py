#!/usr/bin/python3

"""

This is the Initilization module

"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

