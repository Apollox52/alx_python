def raise_exception():
    try:
        raise TypeError("This is a type exception")
    except TypeError as e:
        print("Caught an exception:", e)
