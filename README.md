# python_version_verifier

Simple module to check python version of lambda environment.

## Example Usage

```python
from python_version_verifier import python_3_6_handler


@python_3_6_handler
def lambda_handler():
    """Your lambda function code."""
```

This should be used with a your lambda function logger so any
Exceptions raised by the version verifier are logged

If an exception is triggered due to the python version, the output will be similar to:

```echo
Detected Python 2.7. Python 3.6 or above is required, please update python to v3.6 or higher
```

## Installation

```bash
pip install git+https://github.com/Financial-Times/python-version-verifier.git@master#egg=python_version_verifier
```

or add the following to your requirements.txt

```bash
git+ssh://git@github.com/Financial-Times/python-version-verifier.git@master#egg=python_version_verifier
```

## Licence

This software is published by the Financial Times under the [MIT licence](http://opensource.org/licenses/MIT).

## Notice to non-FT developers

This software is made available by the FT under an MIT licence but, as is our right under that licence, we do not take any responsibility for what you do with it, and currently do not intend to engage with any external efforts to contribute to it. We are always delighted to hear from you if you find it useful, but please understand that we may not respond to issues raised here on GitHub. Open source projects on which we actively engage with the open source community can be found on github.com/ftlabs.
