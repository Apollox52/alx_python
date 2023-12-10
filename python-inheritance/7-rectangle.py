"""
Module containing the Rectangle class, inheriting from BaseGeometry.

Classes:
    Rectangle: A class representing a rectangle, inheriting from BaseGeometry.

Methods:
    None
"""

class BaseGeometry:
    """
    A base class for geometry-related operations.

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented".
        integer_validator(self, name, value): Validates the given integer value.
    """
    def area(self):
        """
        Calculate the area. This method is not implemented in the base class.

        Raises:
            Exception: Always raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the given integer value.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()  # Call the constructor of the BaseGeometry class
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    # Test cases
    r = Rectangle()

    # Case: print(dir(Rectangle))
    print([attr for attr in dir(r) if not callable(getattr(r, attr))])

    # Case: r = Rectangle()
    r = Rectangle()
    print(r)

    # Case: r = Rectangle(1)
    r = Rectangle(1)
    print(r)

    # Case: r = Rectangle(1, [12, 52])
    try:
        r = Rectangle(1, [12, 52])
        print(r)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    # Case: r = Rectangle(4, 5)
    r = Rectangle(4, 5)
    print(r)
    print(r.area())

    # Case: r = Rectangle(4, 5)
    r = Rectangle(4, 5)
    print(r)
    print(r.area())