"""
This module initialize model classes for the AirBnB clone project and handles
class registration.

It imports necessary model classes from the models package, creates a custom
dictionary for handling class registration, and reloads objects from storage
using the FileStorage class.

Attributes:
    storage: An instance of the FileStorage class for handling object
    serialization and deserialization.
    classes: A custom dictionary mapping class names to their corresponding
    class objects.
    Used for class registration and object retrieval.

Classes:
    Classes: A custom dictionary class for handling class registration and
    object retrieval.
             It raises an exception if a class is not found.
"""


try:
    from models.amenity import Amenity
    from models.base_model import BaseModel
    from models.city import City
    from models.engine.file_storage import FileStorage
    from models.place import Place
    from models.review import Review
    from models.state import State
    from models.user import User

    storage = FileStorage()

    class Classes(dict):
        """
        Custom dictionary class for handling class registration and object
        retrieval.

        Methods:
            __getitem__(self, key): Overrides dictionary item retrieval to
            raise an exception if class is not found.
        """
        def __getitem__(self, key):
            """
            Retrieve an item from the dictionary.

            Args:
                key (str): The class name to retrieve.

            Returns:
                object: The class object associated with the given class name.

            Raises:
                Exception: If the specified class is not found.
            """
            try:
                return super(Classes, self).__getitem__(key)
            except KeyError:
                raise Exception("** class doesn't exist **")

    models_list = [BaseModel, Place, State, City, Amenity, Review, User]
    classes = Classes(**{x.__name__: x for x in models_list})

    storage.reload()

except Exception as e:
    print(f"An error occurred: {e}")
