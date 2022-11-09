#!/usr/bin/python3
# A function that executes a function safely


def safe_function(fct, *args):
    from sys import stderr
    try:
        result = fct(*args)
    except Exception as err:
        result = None
        stderr.write("Exception: {}\n".format(err))
    return result
