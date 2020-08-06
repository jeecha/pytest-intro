import pytest

@pytest.fixture(scope="session")
def fixture1():
    print("\nfixture1 initialization")
    yield "i am the resource"
    print("\nfixture1 finalization")

@pytest.fixture(scope="function")
def fixture2():
    print("\nfixture2 initialization")
    yield "i am the resource"
    print("\nfixture2 finalization")

def test(fixture1, fixture2):
    print("\nexecuting test case")

def test2(fixture1, fixture2):
    print("\nexecuting test case 2")

