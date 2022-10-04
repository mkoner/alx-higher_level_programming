#!/usr/bin/python3
"""
Module that defines a rectangle class
with attributes width and height
and instanciation method
"""


class Rectangle:
    """ Defines Rectangle class """

    def __init__(self, width=0, height=0):
        """Initializes the objects"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Modifies the height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the triangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the triangle"""
        if(self.__width == 0 or self.height == 0):
            return 0
        else:
            return 2 * self.__width + 2 * self.__height
