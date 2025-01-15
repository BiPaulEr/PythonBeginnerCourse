import pytest 

def test_simple():
    assert 1 + 1 == 2
    assert 2 in [1, 2, 3]
    assert isinstance("hello", str)
    with pytest.raises(ZeroDivisionError):
        1 / 0
    assert not 5 < 3
    a = dict()
    b = a
    assert a == b
    assert "apple".startswith("a")

