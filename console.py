#!/usr/bin/python3
"""
This module contain the HBNBCommand class which
serves as the command-line interface(CLI) for the AirBnB
clone project.
"""

import cmd

import models


class HBNBCommand(cmd.Cmd):
    """
    Command Line Interpreter class for the AirBnB clone project.

    Attributes:
        intro (str): The introduction message displayed when the shell starts.
        prompt (str): The shell prompt.
    """

    intro = "Type 'help' or '?' for assistance, 'quit' to exit console.\n"
    prompt = "(hbnb): "

    def emptyline(self):
        """
        Handles an empty line input. Does nothing.
        """
        pass

    def do_quit(self, arg):
        """
        Quits the console.
        """
        return True

    def do_EOF(self, arg):
        """
        Quits the console when the EOF signal is received.
        """
        return True

    def do_create(self, arg):
        """
        Creates a new instance of a specified class,
        saves it, and prints the id.
        """
        try:
            if not arg:
                raise ValueError('** class name missing **')

            class_name, *instance_args = arg.split()
            if class_name not in models.classes:
                raise ValueError('** class doesn\'t exist **')

            new_instance = models.classes[class_name](*instance_args)
            models.storage.new(new_instance)
            models.storage.save()
            print(new_instance.id)
            print("instance created successfully")

        except ValueError as e:
            print(e)
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = arg.split()
        if not arg:
            print('** class name missing **')
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        try:
            model_name = args[0]
            model_id = args[1]
            model = models.storage.find(model_name, model_id)
            print(model.__str__())
        except Exception as e:
            print(str(e))

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not arg:
            print('** class name missing **')
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        try:
            model_name = args[0]
            model_id = args[1]
            models.storage.delete(model_name, model_id)
            models.storage.save()
        except Exception as e:
            print(str(e))

    def do_all(self, arg):
        """
        Prints all string representation of instances.
        """
        try:
            if not arg:
                print([str(value) for value in models.storage.all().values()])
            else:
                model_class = models.classes.get(arg)
                if not model_class:
                    print('** class doesn\'t exist **')
                    return
                print([str(value) for value in models.storage.all(
                     model_class).values()]
                     )
        except Exception as e:
            print(str(e))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        args = arg.split()
        if not arg:
            print('** class name missing **')
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        elif len(args) == 2:
            print('** attribute name missing **')
            return
        elif len(args) == 3:
            print('** value missing **')
            return

        try:
            model_name = args[0]
            model_id = args[1]
            attribute = args[2]
            value = args[3].strip('"')
            model = models.storage.find(model_name, model_id)
            if model:
                setattr(model, attribute, value)
                models.storage.save()
            else:
                print('** no instance found **')
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
