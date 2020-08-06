import pytest


def sum(a, b):
    return a + b


@pytest.mark.parametrize("a, b, expected", [
    (2, 5, 7), (10, 20, 30)
], ids=["2plus5equals7", "10plus20equals30"])
def test(a, b, expected):
    assert sum(a, b) == expected

