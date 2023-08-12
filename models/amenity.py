#!/usr/bin/python3
from models.base_model import BaseModel

"""

This module contains the amenity class of the which inherits
from the BaseModel class

"""


class Amenity(BaseModel):
    """The amenity class which has attributes

    methods:
        __init__: the initialization method that initializes the instance

    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize amenity class"""
        super().__init__(**kwargs)
