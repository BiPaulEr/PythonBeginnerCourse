import pytest
from calculator import add, check_value, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_check_value():
    assert check_value(15) == "Big"  # Teste la branche if
    assert check_value(5) == "Small"  # Teste la branche else

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 100) == 0
