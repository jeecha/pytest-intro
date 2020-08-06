import pytest

ARGUMENTS_FOR_TESTS = [(1, 2), (3, 4)]
EXTRA_FOR_TEST2 = [(5, 6)]

def more_arguments():
    return [(7, 10)]

@pytest.mark.parametrize("a, b", ARGUMENTS_FOR_TESTS + more_arguments())
def test(a, b):
    assert True

@pytest.mark.parametrize("a, b", ARGUMENTS_FOR_TESTS + EXTRA_FOR_TEST2)
def test2(a, b):
    assert True
