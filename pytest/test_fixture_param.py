import pytest

@pytest.fixture(params = [1, 2, 3])
def setup_int(request):
    return request.param

@pytest.fixture(params = ["A", "B", "C"])
def setup_str(request):
    return request.param

def test_combined(setup_int, setup_str):
    #print(setup_int, setup_str)
    assert True