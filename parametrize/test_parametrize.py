import pytest


def sum(a, b):
    return a + b


# use pytest.mark.parametrize to provide multiple sets of arguments
# to the test method
@pytest.mark.parametrize("a, b, expected", [(2, 5, 7), (10, 20, 30)])
def test(a, b, expected):
    # test method will be called twice with:
    # a=2, b=5, expected=7
    # a=10, b=20, expected=30
    assert sum(a, b) == expected

