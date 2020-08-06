import pytest

@pytest.fixture
def resource():
    print("\n\nfixture initialization")
    yield "i am the resource"
    print("\n\nfixture finalization")

def test(resource):
    print("\n\nexecuting test case")

