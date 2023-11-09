import uuid
from datetime import datetime
from json import JSONEncoder

import models


class BaseModel:
    """
    BaseModel class for the AirBnB clone project.

    Attributes:
        id (str): This is a unique identifier for every instance.
        created_at (datetime): The date and time when the instance was created.
        updated_at (datetime): The date and time when the instance was last
        updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        If kwargs is provided, instance attributes are initialized with the
        provided values. If not, id is generated, created_at and updated_at
        are set to the current datetime,and the instance is added to the
        storage.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        Saves new information to the class object.

        Updates the updated_at attribute with the current datetime and
        saves the instance.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: A dictionary containing instance attributes.
        """
        dict_repr = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dict_repr[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
            else:
                dict_repr[key] = value
        dict_repr["__class__"] = type(self).__name__
        return dict_repr

    def __str__(self):
        """
        Returns a string formatted message when the instance is called.

        Returns:
            str: A string representation of the instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


class BaseModelEncoder(JSONEncoder):
    """
    JSON Encoder for BaseModel.

    Extends the JSONEncoder class to handle BaseModel objects.
    """

    def default(self, o):
        """
        Default method for JSON encoding.

        Args:
            o: The object to encode.

        Returns:
            obj: Encoded object.
        """
        if isinstance(o, BaseModel):
            return o.to_dict()
        return super().default(o)
