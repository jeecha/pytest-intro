import pytest

@pytest.fixture
def somefixture(request):
    print("fixture initialization")
    yield "i am the fixture"

@pytest.mark.usefixtures("somefixture")
def test():
    # even though the test case does not request the fixture
    # in arguments, it will still be created
    print("\nexecuting test case")
