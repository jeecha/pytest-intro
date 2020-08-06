import pytest

@pytest.fixture
def resource():
    print("\nfixture initialization")
    yield "i am the resource"
    print("\nfixture finalization")

def test(resource):
    print("\nexecuting test case")



