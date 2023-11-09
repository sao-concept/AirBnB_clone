#!/usr/bin/python3
"""
Module containing the State class, a subclass of BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class representing states in the AirBnB clone project.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a State instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Note:
            Uses the __init__ method of the parent BaseModel class.
            Initializes attributes to default values.
        """
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        """
        Returns the string representation of the State instance.

        Returns:
            str: Formatted string representing the State instance.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.name
                )
