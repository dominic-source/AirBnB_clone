#!/usr/bin/python3
"""

This Module contains classes an method for filestorage using
serialization an deserialization of instances

"""
import json


class FileStorage():
    """The file storage class

    This class stores, creates, retrieves and destroys object

    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """This method will return the dictionary object"""

        return FileStorage.__objects

    def new(self, obj):
        """
        set the a value in  __objects using <obj class name>.id as the key
        """

        mkey = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[mkey] = obj

    def save(self):
        """This method will serialize __object to the json file in path"""

        dictme = dict()
        for key, value in FileStorage.__objects.items():
            dictme[key] = value.to_dict()
        json_string = json.dumps(dictme)
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file1:
            file1.write(json_string)

    def classes(self):
        """Return the class object to be use for object creation"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        my_obj = {"BaseModel": BaseModel, "User": User, 'Place': Place,
                  'State': State, 'City': City, 'Amenity': Amenity,
                  'Review': Review}
        return my_obj

    def reload(self):
        """Reloads the json file to __objects if the __file_path exist"""

        listModels = self.classes()
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as fileJ:
                obj_str = fileJ.read()
                my_dict = json.loads(obj_str)
                FileStorage.__objects = {}
                for key, value in my_dict.items():
                    newkey = key.split('.')[0]
                    newvalue = listModels[newkey](**value)
                    FileStorage.__objects[key] = newvalue

        except FileNotFoundError:
            pass
