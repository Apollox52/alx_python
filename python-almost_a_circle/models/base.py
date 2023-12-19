class Base:
    """
    Base class for managing id attribute in all classes.

    Attributes:
    - id (int): Public instance attribute representing the object identifier.
    """

    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
        - id (int, optional): Object identifier. If provided, assign to the id attribute.
            If not provided, increment __nb_objects and assign the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects