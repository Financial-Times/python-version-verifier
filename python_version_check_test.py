import pytest
import sys

import python_version_check
from python_version_check import require_python_3_6


@pytest.mark.parametrize("major,minor", [ (3, 6), (3, 7) ])
def test_requirement_satisfied_with_python_version_3_6_or_higher(major, minor):
    python_version_check.python_version = (major, minor)
    require_python_3_6()


@pytest.mark.parametrize("major,minor", [ (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5) ])
def test_requirement_is_not_satisfied_with_python_versions_prior_to_3_6(major, minor):
    python_version_check.python_version = (major, minor)
    with pytest.raises(Exception):
        require_python_3_6()


@pytest.mark.parametrize("major,minor", [ (2, 6), (2, 7) ])
def test_requirement_is_not_satisfied_with_major_version_2(major, minor):
    python_version_check.python_version = (major, minor)
    with pytest.raises(Exception):
        require_python_3_6()


@pytest.mark.parametrize("major,minor", [ (4, 0) ])
def test_requirement_satisfied_with_python_version_3_6_or_higher(major, minor):
    python_version_check.python_version = (major, minor)
    with pytest.raises(Exception):
        require_python_3_6()


@pytest.mark.parametrize("required_major,required_minor", [ (3, 6) ])
@pytest.mark.parametrize("major,minor", [ (4, 0), (2, 6), (3, 5) ])
def test_error_message_returned_on_exception(major, minor, required_major, required_minor):
    python_version_check.python_version = (major, minor)
    with pytest.raises(Exception) as exception_resp:
        require_python_3_6()
    expected_error_msg = 'Detected Python {0}.{1}. '\
        'Python {2}.{3} or above is required, '\
        'please update python to v{2}.{3} or higher'\
        .format(major, minor, required_major, required_minor)

    assert str(exception_resp.value) == expected_error_msg


@pytest.mark.parametrize("required_major,required_minor", [ (3, 6) ])
@pytest.mark.parametrize("major,minor", [ (3, 5) ])
def test_required_parameters_returned_on_exception(major, minor, required_major, required_minor):
    python_version_check.python_version = (major, minor)
    with pytest.raises(Exception) as exception_resp:
        require_python_3_6()
    expected_error_msg = 'Detected Python {0}.{1}. '\
        'Python {2}.{3} or above is required, '\
        'please update python to v{2}.{3} or higher'\
        .format(major, minor, required_major, required_minor)

    assert str(exception_resp.value) == expected_error_msg


@pytest.mark.parametrize("required_major,required_minor", [ (3, 6), (3, 5) ])
@pytest.mark.parametrize("major,minor", [ (3, 6), (3, 7) ])
def test_required_parameters_return_successful(major, minor, required_major, required_minor):
    python_version_check.python_version = (major, minor)
    require_python_3_6(required_major, required_minor)
