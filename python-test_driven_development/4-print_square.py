#!/usr/bin/python3
"""Module for printing a square with the character #."""


def print_square(size):
    """Print a square of size x size made of '#' characters."""
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
