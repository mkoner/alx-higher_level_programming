#!/usr/bin/python3
"""
Define a square class
Initializes it and checks the size attribute
returns the area of the square
Print the square with #
"""


class Square:
    """Square class implementation"""

    def __init__(self, size=0):
        """Initializing the square object"""
        self.size = size

    @property
    def size(self):
        """Retrieves the attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Modifies the attribute size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
