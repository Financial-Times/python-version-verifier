"""Decorator to verify version of python running."""
import sys
from functools import wraps


def require_python(python_version, required_major, required_minor):
    """Python version verify."""
    try:
        major_version = python_version[0]
        minor_version = python_version[1]

        error_msg = 'Detected Python {0}.{1}. '\
            'Python {2}.{3} or above is required, '\
            'please update python to v{2}.{3} or higher'\
            .format(major_version, minor_version, required_major, required_minor)

        if major_version != required_major:
            raise Exception(error_msg)

        if minor_version < required_minor:
            raise Exception(error_msg)

        print(python_version)
    except Exception as err:
        print("{}".format(err))
        raise err


def python_3_6_handler(function):
    """Decorator."""
    @wraps(function)
    def wrapper(*args, **kwargs):
        py_version = sys.version_info
        require_python(py_version, 3, 6)
        return function(*args, **kwargs)
    return wrapper
