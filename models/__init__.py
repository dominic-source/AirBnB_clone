#!/usr/bin/python3
"""
Initialization module to initialize and reload the file storage engine

"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
