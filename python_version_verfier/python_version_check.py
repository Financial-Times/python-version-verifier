import sys
from functools import wraps

python_version = sys.version_info


def require_python_3_6(required_major=3, required_minor=6):

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


def python_3_6_handler(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            require_python_3_6()
            function(*args, **kwargs)
        except Exception as err:
            print("{}".format(err))
    return wrapper
