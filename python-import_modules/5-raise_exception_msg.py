def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError as ne:
        print(ne)

raise_exception_msg("C is fun")
raise_exception_msg("python is cool")
raise_exception_msg("")