import sys
from functools import wraps


def require_python_3_6(python_version, required_major=3, required_minor=6):
    try:
        major_version = python_version[0]
        minor_version = python_version[1]

        error_msg = 'Detected Python {0}.{1}. '\
            'Python {2}.{3} or above is required, '\
            'please update python to v{2}.{3} or higher'\
            .format(major_version, minor_version, required_major, required_minor)

        if (major_version != required_major):
            raise Exception(error_msg)

        if (minor_version < required_minor):
            raise Exception(error_msg)

        print(python_version)
    except Exception as err:
        print("{}".format(err))
        raise err

def python_3_6_handler(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        py_version = sys.version_info
        require_python_3_6(python_version=py_version)
        function(*args, **kwargs)
    return wrapper
