#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a user-friendly string representation of the square.

        Returns:
            str: Description formatted as [Square] <width>/<height>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
