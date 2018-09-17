import os
import sys

HERE = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(HERE, "../"))

from python_version_verifier import *


@python_3_6_handler
def lambda_handler(event, context):
    message = {"message": "version check passed"}
    print("version check passed")
    return message


if __name__ == "__main__":
    lambda_handler(None, None)
