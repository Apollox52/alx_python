"""
models: A package for managing objects in the project.

This package contains modules for defining base classes and other related functionality.

Modules:
    - base: Contains the Base class for managing object identifiers.
"""
class Base:
    """
    Base class for managing id attribute in all classes.

    Attributes:
        - id (int): Public instance attribute representing the object identifier.
    """

    __nb_objects = 0
    """
    Private class attribute to keep track of the number of objects created.

    This attribute is used to generate unique identifiers for objects.
    """

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int, optional): Object identifier. If provided, assign to the id attribute.
                If not provided, increment __nb_objects and assign the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects