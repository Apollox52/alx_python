"""
Main script to demonstrate the usage of BaseGeometry class.
"""

BaseGeometry = __import__('base_geometry').BaseGeometry

if __name__ == "__main__":
    # Example usage
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    # Additional case
    print(dir(bg))