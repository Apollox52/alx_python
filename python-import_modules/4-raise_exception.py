def raise_exception():
    try:
        {} + "string"
    except TypeError as e:
        print("Caught an exception:", e)