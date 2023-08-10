#!/usr/bin/python3
import json

"""

This Module contains classes an method for filestorage using
serialization an deserialization of instances

"""

class FileStorage():
    """The file storage class"""
    
    __file_path = 'file.json'
    __objects = dict()


    def __init__(self):
        """Initialize the file storage"""
        pass

    def all(self):
        """This method will return the dictionary object"""

        return FileStorage.__objects

    def new(self, obj):
        """set the a value in  __objects using <obj class name>.id as the key"""

        mkey = obj['__class__'] + '.' + obj['id']
        FileStorage.__objects[mkey] = obj

    def save(self):
        """This method will serialize __object to the json file in path"""

        json_string = json.dumps(FileStorage.__objects)

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            file.write(json_string)

    def reload(self):
        """Reloads the json file to __objects if the __file_path exist"""

        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_str = file.read()
                FileStorage.__objects = json.loads(obj_str)
        except FileNotFoundError:
            pass

