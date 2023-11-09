#!/usr/bin/python3
"""
Module containing the Amenity class, a subclass of BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class for representing amenities in the AirBnB clone project.

    Attributes:
        name (str): The name of the amenity.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an Amenity instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Note:
            Uses the __init__ method of the parent BaseModel class.
            Initializes the 'name' attribute to an empty string.
        """
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        """
        Returns the string representation of the Amenity instance.

        Returns:
            str: Formatted string representing the Amenity instance.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.name
                )
