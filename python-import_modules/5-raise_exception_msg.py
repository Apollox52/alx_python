def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError as ne:
        if ne.args and ne.args[0]:
            print(ne.args[0])
        else:
            print(message)


raise_exception_msg("C is fun")
raise_exception_msg("Python is cool")
raise_exception_msg()