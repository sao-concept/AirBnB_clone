import json
import os

import models


class Objects(dict):
    """
    Custom dictionary class for handling objects.

    This class extends the built-in dict class to provide custom handling of
    objects. It raises custom exceptions for missing instances when accessing
    keys or popping items.
    """

    def __getitem__(self, key):
        """
        Retrieve an item from the dictionary.

        Args:
            key (str): The key to retrieve.

        Returns:
            object: The object associated with the given key.

        Raises:
            KeyError: If the specified key is not found.
        """
        try:
            return super(Objects, self).__getitem__(key)
        except KeyError:
            raise KeyError("** no instance found **")

    def pop(self, key, default=None):
        """
        Remove and return an item from the dictionary.

        Args:
            key (str): The key to remove.

        Returns:
            object: The object associated with the given key.

        Raises:
            KeyError: If the specified key is not found.
        """
        try:
            return super(Objects, self).pop(key, default)
        except KeyError:
            raise KeyError("** no instance found **")


class FileStorage:
    """
    Handles serialization and deserialization of instances.

    This class manages the serialization and deserialization of instances to
    and from a JSON file. It provides methods for creating, updating,
    retrieving, and deleting objects.
    """

    FILE_PATH = "file.json"

    def __init__(self):
        """
        Initialize FileStorage instance.

        Initializes the objects dictionary for storing instances.
        """
        self.__objects = Objects()

    def all(self, cls=None):
        """
        Return a dictionary of objects of a specific class (if provided),
        or all objects in the storage.

        Args:
            cls (class, optional): The class type to filter objects.
            Defaults to None.

        Returns:
            dict: A dictionary of objects filtered by class, or all objects
            if class is None.
        """
        if cls is None:
            return self.__objects
        else:
            filtered_objects = {}
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    filtered_objects[key] = obj
            return filtered_objects

    def reset(self):
        """
        Clear data in the objects dictionary (cache).

        Resets the objects dictionary to an empty state.
        """
        self.__objects.clear()

    def new(self, obj):
        """
        Add object to the objects dictionary.

        Args:
            obj (object): The object to add to the dictionary.

        Raises:
            TypeError: If the object is None.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serialize objects to the JSON file.

        Serializes the objects dictionary to a JSON file.
        """
        with open(FileStorage.FILE_PATH, mode="w", encoding="utf-8") as f:
            json.dump(
                {key: obj.to_dict() for key, obj in self.__objects.items()},
                f,
                default=models.base_model.BaseModelEncoder
            )

    def reload(self):
        """
        Deserialize JSON file to objects dictionary.

        Deserializes the JSON file to populate the objects dictionary.
        If the file does not exist, resets the objects dictionary.
        """
        file_path = FileStorage.FILE_PATH
        if os.path.exists(file_path):
            with open(file_path, mode="r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    for object_key, model_data in data.items():
                        model_name, model_id = object_key.split('.')
                        model_class = models.classes[model_name]
                        model_instance = model_class(**model_data)
                        self.new(model_instance)
                except Exception as e:
                    print(e)
        else:
            # If the file does not exist, reset the objects dictionary
            self.__objects = Objects()

    def update(self, obj_name, obj_id, attr, value):
        """
        Update object attribute with new value.

        Args:
            obj_name (str): The class name of the object.
            obj_id (str): The ID of the object.
            attr (str): The attribute to update.
            value (any): The new value for the attribute.

        Raises:
            KeyError: If the specified object is not found.
        """
        object_key = "{}.{}".format(obj_name, obj_id)
        if object_key in self.__objects:
            setattr(self.__objects[object_key], attr, value)
            self.save()
        else:
            raise KeyError("** no instance found **")

    def find(self, obj_name, obj_id):
        """
        Find object with given class name and id.

        Args:
            obj_name (str): The class name of the object.
            obj_id (str): The ID of the object.

        Returns:
            object: The found object, or None if not found.
        """
        return self.__objects.get("{}.{}".format(obj_name, obj_id), None)

    def delete(self, obj_name, obj_id):
        """
        Delete object with given class name and id.

        Args:
            obj_name (str): The class name of the object.
            obj_id (str): The ID of the object.

        Returns:
            object: The deleted object, or raises KeyError if not found.
        """
        object_key = "{}.{}".format(obj_name, obj_id)
        if object_key in self.__objects:
            deleted_obj = self.__objects.pop(object_key)
            self.save()
            return deleted_obj
        else:
            raise KeyError("** no instance found **")
