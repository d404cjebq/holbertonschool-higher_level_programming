#!/usr/bin/python3
"""Module that contains add_integer function."""
def add_integer(a, b=98):
    """Add two integers and return the result.

    Args:
        a: First integer or float.
        b: Second integer or float (default 98).

    Returns:
        The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
