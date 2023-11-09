#!/usr/bin/python3
"""
Module containing the User class, a subclass of BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class representing users in the AirBnB clone project.

    Attributes:
        email (str): Email address of the user.
        password (str): Password of the user.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a User instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Note:
            Uses the __init__ method of the parent BaseModel class.
            Initializes attributes to default values.
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        """
        Returns the string representation of the User instance.

        Returns:
            str: Formatted string representing the User instance.
        """
        return "[{}] ({}) {} {}".format(
            self.__class__.__name__, self.id, self.first_name, self.last_name
        )
