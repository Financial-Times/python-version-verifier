"""Unit tests to validate python version verifier."""
import sys
import os
import pytest

PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, PATH + '/../')

import python_version_verifier
from python_version_verifier import require_python


required_major = 3
required_minor = 6


@pytest.mark.parametrize("py_version", [(3, 6), (3, 7)])
def test_requirement_satisfied_with_python_version_3_6_or_higher(py_version):
    require_python(py_version, required_major, required_minor)


@pytest.mark.parametrize("py_version", [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)])
def test_requirement_is_not_satisfied_with_python_versions_prior_to_3_6(py_version):
    with pytest.raises(Exception):
        require_python(py_version, required_major, required_minor)


@pytest.mark.parametrize("py_version", [(2, 6), (2, 7)])
def test_requirement_is_not_satisfied_with_major_version_2(py_version):
    with pytest.raises(Exception):
        require_python(py_version, required_major, required_minor)


@pytest.mark.parametrize("py_version", [(4, 0)])
def test_requirement_satisfied_with_python_version_3_6_or_higher(py_version):
    with pytest.raises(Exception):
        require_python(py_version, required_major, required_minor)


@pytest.mark.parametrize("py_version", [(4, 0), (2, 6), (3, 5)])
def test_error_message_returned_on_exception(py_version):
    with pytest.raises(Exception) as exception_resp:
        require_python(py_version, required_major, required_minor)
    expected_error_msg = 'Detected Python {0}.{1}. '\
        'Python {2}.{3} or above is required, '\
        'please update python to v{2}.{3} or higher'\
        .format(py_version[0], py_version[1], required_major, required_minor)

    assert str(exception_resp.value) == expected_error_msg


@pytest.mark.parametrize("py_version", [(3, 5)])
def test_required_parameters_returned_on_exception(py_version):
    with pytest.raises(Exception) as exception_resp:
        require_python(py_version, required_major, required_minor)
    expected_error_msg = 'Detected Python {0}.{1}. '\
        'Python {2}.{3} or above is required, '\
        'please update python to v{2}.{3} or higher'\
        .format(py_version[0], py_version[1], required_major, required_minor)

    assert str(exception_resp.value) == expected_error_msg


@pytest.mark.parametrize("required_major,required_minor", [(3, 6), (3, 5)])
@pytest.mark.parametrize("py_version", [(3, 6), (3, 7)])
def test_required_parameters_return_successful(py_version, required_major, required_minor):
    print("required_major: {},required_minor: {}".format(required_major, required_minor))
    print("py_version: {}".format(py_version))
    require_python(py_version, required_major, required_minor)
