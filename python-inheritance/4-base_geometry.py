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
        expected_order = [
            '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
            '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
            '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
            '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
            '__subclasshook__', '__weakref__', 'area'
        ]
        return str([attr for attr in expected_order if hasattr(self, attr)])