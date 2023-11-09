#!/usr/bin/python3
"""
Module containing the City class, a subclass of BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for representing cities in the AirBnB clone project.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a City instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Note:
            Uses the __init__ method of the parent BaseModel class.
            Initializes the 'state_id' attribute to an empty string and the
            'name' attribute to an empty string.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""

    def __str__(self):
        """
        Returns the string representation of the City instance.

        Returns:
            str: Formatted string representing the City instance.
        """
        return "[{}] ({}) {} - {}".format(
            self.__class__.__name__, self.id, self.name, self.state_id
        )
