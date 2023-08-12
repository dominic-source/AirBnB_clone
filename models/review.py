#!/usr/bin/python3
"""

This module contains the review class of the which inherits
from the BaseModel class

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The review class which has attributes

    methods:
        __init__: the initialization method that initializes the instance

    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize review class which is a subclass of the BaseModel"""

        super().__init__(**kwargs)
