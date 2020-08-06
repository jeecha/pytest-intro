import pytest

@pytest.fixture(autouse=True)
def somefixture(request):
    print("fixture initialization")
    yield "i am the fixture"

def test():
    print("\nexecuting test case")



