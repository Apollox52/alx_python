"""
models/square.py

Square module defining the Square class, which inherits from the Rectangle class.

Classes:
    - Square: Represents a square, inherits attributes and methods from Rectangle.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class, inherits from Rectangle class.

    Attributes:
        - id (int): Public instance attribute representing the object identifier.
        - size (int): Private instance attribute representing the size of the square.
        - x (int): Private instance attribute representing the x-coordinate of the square.
        - y (int): Private instance attribute representing the y-coordinate of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        Args:
            size (int): Size of the square.
            x (int, optional): x-coordinate of the square. Defaults to 0.
            y (int, optional): y-coordinate of the square. Defaults to 0.
            id (int, optional): Object identifier. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size.

        Args:
            value (int): Value to set as the size of the square.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If size is under or equals 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: String representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)