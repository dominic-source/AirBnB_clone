#!/usr/bin/python3

"""
Initialization module

"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
