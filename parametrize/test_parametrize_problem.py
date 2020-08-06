import pytest


def sum(a, b):
    return a + b


def test1():
    assert sum(2, 5) == 7


def test2():
    assert sum(10, 20) == 30


# we have a lot of code duplication, and we will need to keep
# adding new test cases if we want to test the method with
# more argument combinations
