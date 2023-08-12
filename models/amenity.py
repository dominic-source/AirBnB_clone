#!/usr/bin/python3
"""

This module contains the amenity class of the which inherits
from the BaseModel class

"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The amenity class which has attributes

    methods:
        __init__: the initialization method that initializes the instance

    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize amenity class which is a subclass of the BaseModel"""

        super().__init__(**kwargs)
