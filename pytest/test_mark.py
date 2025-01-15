import pytest
import sys

@pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (4, 5, 9), (10, 20, 30)])
def test_addition(x, y, expected):
    assert x + y == expected

@pytest.mark.skip(reason = "Non-supporter")
def test_to_skip():
    assert False

@pytest.mark.skipif("sys.platform == 'win32'", reason="Test non supporté sous Windows")
def test_for_linux():
    assert True

@pytest.mark.xfail
def test_expected_failure():
    assert 1 + 1 == 3

@pytest.mark.unit
def test_addition():
    assert 1 + 1 == 2

@pytest.mark.integration
def test_integration_database():
    assert True