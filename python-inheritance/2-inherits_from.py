"""This module defines a function to check if an object is an instance of a class that inherited
(directly or indirectly) from the specified class."""

def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a class that inherited from a_class, False otherwise.
    """
    return type(obj) is a_class or issubclass(type(obj), a_class)