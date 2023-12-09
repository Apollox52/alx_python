"""This module defines a Square class.

This class represents a square with a given size.

Attributes:
    __size (int): The size of the square.
"""

class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance with an optional size.
        area(self): Returns the current square area.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
