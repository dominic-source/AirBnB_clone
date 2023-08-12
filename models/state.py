#!/usr/bin/python3
"""

This module contains the state class of the which inherits
from the BaseModel class

"""
from models.base_model import BaseModel


class State(BaseModel):
    """

    The state class which has attributes
    attributes:
        __init__: the initialization method that initializes the instance

    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize state class which is a subclass of the BaseModel"""

        super().__init__(**kwargs)
