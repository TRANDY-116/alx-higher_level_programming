#!/usr/bin/python3

""" This is a module that defines a class Rectangle """


class Rectangle:
    """ Creation of the class named Rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initializing the rectangle with the width and height.

        Args:
            width: The width of the rectangle (default: 0).
            height: The height of the rectangle(default: 0).

        Raises:
            TypeError: If the area of the rectangle isn't an integer.
            ValueError: If the area of the rectangle is less than zero
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ To retrieve the width of the class """

        return self.__width

    @width.setter
    def width(self, value):
        """ To Set the width of the class """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """ To retrieve the height of the rectangle """

        return self.__height

    @height.setter
    def height(self, value):
        """ To set the height of the class """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ To return the area of the rectangle """

        return self.__width * self.__height

    def perimeter(self):
        """ To return the perimeter of the rectangle """

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ To return the string representation of the rectangle using # """

        if self.__width == 0 or self.__height == 0:
            return ''

        rectangle = ''
        for row in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width + '\n'

        return rectangle[:-1]

    def __repr__(self):
        """ To return string represeentation of the rectangle"""

        return ('Rectangle({:d}, {:d})'.format(self.__width, self.__height))

    def __del__(self):
        """ To print the message 'Bye Rectangle...'
        after deleting an instance """

        print('Bye rectangle...')

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Static method that returns the biggest rectangle based on area """

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1

        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Class method that returns a new square instance in our class """

        return Rectangle(size, size)
