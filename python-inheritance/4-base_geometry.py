"""
Module containing the BaseGeometry class for geometry-related operations.
"""

class BaseGeometry:
    """
    Base class for geometry-related operations.

    Attributes:
        None

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented".
    """
    def area(self):
        """
        Calculate the area. This method is not implemented in the base class.

        Raises:
            Exception: Always raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def __str__(self):
        """
        String representation of the BaseGeometry instance.

        Returns:
            str: String representation including information about the class.
        """
        return str(dir(self))
