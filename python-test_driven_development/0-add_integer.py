#!/usr/bin/python3
"""
This "0-add_integer" module supplies function, add_integer(a, b).
"""


def add_integer(a, b):
    """Return the addtion of the two."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type (b) is not int and type(b) is not a float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
