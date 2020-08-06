import pytest

@pytest.fixture(scope="session")
def resource():
    print("\nfixture initialization")
    yield "i am the resource"
    print("\nfixture finalization")

def test(resource):
    print("\nexecuting test case")

def test2(resource):
    print("\nexecuting test case 2")

