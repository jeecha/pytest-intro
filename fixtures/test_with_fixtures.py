import pytest


@pytest.fixture
def resource():
    return "i am the resource"


def test(resource):
    print(resource)


def test2(resource):
    print(resource)

