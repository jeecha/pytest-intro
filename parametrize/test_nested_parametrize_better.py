import pytest

@pytest.mark.parametrize("a, b", [(1, 2), (3, 4)])
def test(a, b):
    assert True

@pytest.mark.parametrize("a, b", [(1, 2), (3, 4)])
def test2(a, b):
    assert True
