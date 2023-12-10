"""
Module containing the Rectangle class, inheriting from BaseGeometry.
"""

from 5-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """
        String representation of the Rectangle instance.

        Returns:
            str: String representation including information about width and height.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)