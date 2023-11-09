#!/usr/bin/python3
"""
Module containing the Review class, a subclass of BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class representing reviews in the AirBnB clone project.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a Review instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Note:
            Uses the __init__ method of the parent BaseModel class.
            Initializes attributes to default values.
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    def __str__(self):
        """
        Returns the string representation of the Review instance.

        Returns:
            str: Formatted string representing the Review instance.
        """
        return "[{}] ({}) {} - {}".format(
            self.__class__.__name__, self.id, self.text, self.place_id
        )
