# python_version_verifier
Simple module to check python version of lambda environment.

## Example Usage:
```
from python_version_verifier import *

@python_3_6_handler
def lambda_handler():
  # Your lambda function code

```
This should be used with a your lambda function logger so any
Exceptions raised by the version verifier are logged

If an exception is triggered due to the python version, the output will be similar to:

```
Detected Python 2.7. Python 3.6 or above is required, please update python to v3.6 or higher

```

## Installation

pip install git+https://github.com/Financial-Times/python-version-verifier.git@master#egg=python_version_verifier

or add the following to your requirements.txt

git+https://github.com/Financial-Times/python-version-verifier.git@master#egg=python_version_verifier
