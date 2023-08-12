#!/usr/bin/python3
from models.base_model import BaseModel

"""

This module contains the user class of the which inherits
from the BaseModel class

"""


class City(BaseModel):
    """The city class is the city of the user

    methods:
        __init__: the initialization method that initializes the instance

    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize city class"""
        super().__init__(**kwargs)
