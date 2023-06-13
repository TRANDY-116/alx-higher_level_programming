#!/usr/bin/python3

""" Module that adds a new attribute to an object if possible"""


def add_attribute(obj, name, val):
    """
        Function to add new attributes

        Args:
            obj: the object where the attribute will be added to
            name: The name atttribute we are adding
            val: The value of the attribute we are adding

        Raises:
            TypeError: if the object can't have a new attribute
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError('can\'t add new attribute')

    setattr(obj, name, val)
