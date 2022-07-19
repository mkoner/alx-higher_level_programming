#!/usr/bin/python3
"""Define a square class with attribute size"""


class Square:
    """Represents a square with size"""

    def __init__(self, size=0):
        """Initializes the square"""

        if(size < 0):
            raise ValueError("size must be >= 0")
        elif(type(size) != <classe 'int'>):
            raise TypeError("size must be an integer")
        else:
            self.__size = size
