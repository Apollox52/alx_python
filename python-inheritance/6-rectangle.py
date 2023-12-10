"""
Module containing the Rectangle class, inheriting from BaseGeometry.
"""

from base_geometry import BaseGeometry

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
        super().__init__()  # Call the constructor of the BaseGeometry class
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

if __name__ == "__main__":
    # Example usage
    Rectangle = __import__('6-rectangle').Rectangle

    r = Rectangle(3, 5)

    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))