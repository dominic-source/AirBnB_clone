#!/usr/bin/python3
"""

This module contains the user class of the which inherits
from the BaseModel class

"""
from models.base_model import BaseModel


class User(BaseModel):
    """

    The user class which has attributes
    attributes:
        __init__: the initialization method that initializes the instance

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize user class which is a subclass of the BaseModel"""

        super().__init__(**kwargs)
