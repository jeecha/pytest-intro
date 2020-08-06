import pytest

def sum(a, b):
    return a + b

@pytest.mark.parametrize("a, b, expected", [
    pytest.param(2, 5, 7, marks=pytest.mark.skip), 
    pytest.param(10, 20, 30)
])
def test(a, b, expected):
    assert sum(a, b) == expected

