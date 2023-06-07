#!/usr/bin/python3
""" A module that prevents users from dynamically creating new instances """


class LockedClass:
    """
    Initialization of the class that only lets instanced called
    first_name to be created
     """
    __slots__ = ["first_name"]
