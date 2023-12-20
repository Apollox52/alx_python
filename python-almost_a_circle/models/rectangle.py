"""
models: A package for managing objects in the project.

This package contains modules for defining base classes and other related functionality.

Modules:
    - base: Contains the Base class for managing object identifiers.
    - rectangle: Contains the Rectangle class, which inherits from the Base class and represents rectangles.
"""

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class, inherits from Base class.

    Attributes:
        - id (int): Public instance attribute representing the object identifier.
        - width (int): Private instance attribute representing the width of the rectangle.
        - height (int): Private instance attribute representing the height of the rectangle.
        - x (int): Private instance attribute representing the x-coordinate of the rectangle.
        - y (int): Private instance attribute representing the y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): Object identifier. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width.

        Args:
            value (int): Value to set as the width of the rectangle.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If width is under or equals 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height.

        Args:
            value (int): Value to set as the height of the rectangle.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If height is under or equals 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x.

        Args:
            value (int): Value to set as the x-coordinate of the rectangle.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If x is under 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y.

        Args:
            value (int): Value to set as the y-coordinate of the rectangle.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If y is under 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """Print the rectangle using the '#' character, considering x and y offsets."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Update attributes of the rectangle.

        Args:
            *args: Variable number of arguments representing id, width, height, x, y.
            **kwargs: Variable number of keyword arguments representing attributes.

        Note:
            Argument order is not important.
            **kwargs must be skipped if *args exists and is not empty.
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)