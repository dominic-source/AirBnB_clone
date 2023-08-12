#!/usr/bin/python3
from models.base_model import BaseModel

"""

This module contains the place class of the which inherits
from the BaseModel class

"""


class Place(BaseModel):
    """The place class which has attributes

    methods:
        __init__: the initialization method that initializes the instance

    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize place class"""
        super().__init__(**kwargs)
