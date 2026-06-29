#!/usr/bin/env python3
"""Module for CustomObject class with pickle serialization."""
import pickle


class CustomObject:
    """A custom object that can be serialized and deserialized with pickle."""

    def __init__(self, name, age, is_student):
        """Initializes a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the current instance and saves it to a file."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and returns a CustomObject instance from a file."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
