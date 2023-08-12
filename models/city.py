#!/usr/bin/python3
"""

This module contains the user class of the which inherits
from the BaseModel class

"""
from models.base_model import BaseModel


class City(BaseModel):
    """

    The city class is the city of the user
    attributes:
        __init__: the initialization method that initializes the instance

    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize city class which is a subclass of the BaseModel"""

        super().__init__(**kwargs)
