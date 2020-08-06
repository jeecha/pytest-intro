import pytest

@pytest.fixture(scope="session")
def resource():
    print("\nfixture initialization")
    yield "i am the resource"
    print("\nfixture finalization")

@pytest.fixture
def another_resource(resource):
    print("\nanother_resource init")
    yield "i am another resource"
    print("\nanother_resource finit")

def test(another_resource):
    print("\nexecuting test case")

def test2(another_resource):
    print("\nexecuting test case 2")


