Airbnb Clone Project

This project is an implementation of an Airbnb clone, focusing on the backend infrastructure and command-line interface. It provides functionalities similar to Airbnb, allowing users to interact with different models such as BaseModel, Amenity, City, Place, Review, State, and User through a command-line interface.

Command Interpreter

The command interpreter, console.py, serves as the primary interface for interacting with the Airbnb clone. It allows users to create, read, update, and delete instances of the supported models. Below are instructions on how to start and use the command interpreter.

How to Start

To start the command interpreter, run the following command in your terminal:

$ python3 console.py
This will launch the Airbnb command-line interface, allowing you to enter commands and interact with the models.

How to Use

Once the command interpreter is running, you can use the following commands:

create <class_name>: Creates a new instance of the specified class.
show <class_name> <id>: Displays the string representation of an instance based on the class name and ID.
destroy <class_name> <id>: Deletes an instance based on the class name and ID.
all [class_name]: Displays the string representation of all instances or specific class instances.
update <class_name> <id> <attribute_name> "<attribute_value>": Updates the specified attribute of an instance based on the class name and ID.

Examples
Creating a new User instance:

(hbnb) create User
Showing details of a specific Place instance:
scss

(hbnb) show Place 1234-5678
Updating the email of a User instance:
sql

(hbnb) update User 1234-5678 email "newemail@example.com"
Listing all instances of a specific class:
scss

(hbnb) all User
