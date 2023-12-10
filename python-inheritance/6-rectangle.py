"""
Module containing the BaseGeometry class for geometry-related operations.

Classes:
    BaseGeometry: A base class for geometry-related operations.

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
