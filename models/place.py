#!/usr/bin/python3
"""
Module containing the Place class, a subclass of BaseModel.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class representing places in the AirBnB clone project.

    Attributes:
        city_id (str): The ID of the city where the place is located.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): Description of the place.
        number_rooms (int): Number of rooms in the place.
        number_bathrooms (int): Number of bathrooms in the place.
        max_guest (int): Maximum number of guests the place can accommodate.
        price_by_night (int): Price per night to stay at the place.
        latitude (float): Latitude coordinates of the place.
        longitude (float): Longitude coordinates of the place.
        amenity_ids (list): List of Amenity IDs associated with the place.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a Place instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Note:
            Uses the __init__ method of the parent BaseModel class.
            Initializes attributes to default values.
        """
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

    def __str__(self):
        """
        Returns the string representation of the Place instance.

        Returns:
            str: Formatted string representing the Place instance.
        """
        return "[{}] ({}) {} - {}".format(
            self.__class__.__name__, self.id, self.name, self.city_id
        )
