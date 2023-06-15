#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Reads the file to UTF8"""

    with open(filename, mode='r', encoding='utf-8') as read_file:
        print(read_file.read(), end= "")
