#!/usr/bin/python3

"""
Module for add_integer function.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int): The first integer.
        b (int, optional): The second integer. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if b is not None and not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
