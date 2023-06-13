#!/usr/bin/python3

""" Module of a class MyInt that inherits int """


class MyInt(int):
    """ class that inherits int """

    def __eq__(self, equal):
        """
            Function to invert the rebelion in the MyInt class

            Args:
                equal: the equality sign to invert
        """

        return super().__ne__(equal)

    def __ne__(self, equal):
        """
            Function that inverts the rebelion in MyInt class

            Args:
                equal: the equality sign to invert
        """

        return super().__eq__(equal)
