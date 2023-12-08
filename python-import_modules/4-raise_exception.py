def raise_exception():
    try:
        raise TypeError("Exception raised")
    except TypeError as t:
        print(t)

raise_exception()