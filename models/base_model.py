#!/usr/bin/python3
import uuid
from datetime import datetime

"""Base model class

This class will be the base class for all the models that will be created

"""


class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initialize the id, and instance of created_at or updated_at"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints out the class name, id and dictionary of the class"""

        return '[{}] ({}) {}'.format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update the public instance attribute updated_at"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """create a dictionary from the object"""

        my_dict = self.__dict__
        my_dict.update(__class__=type(self).__name__)
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        my_dict['created_at'] = my_dict['created_at'].isoformat()

        return my_dict
