import pytest

@pytest.mark.parametrize("a, b", [
    (1, 2),
    (1, 5),
    (1, 7),
    (2, 2),
    (2, 5),
    (2, 7),
])
def test(a, b):
    assert True
