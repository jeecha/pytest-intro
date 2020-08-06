import pytest

@pytest.fixture(params=["chrome", "firefox"])
def resource(request):
    print("\nfixture initialization: {}".format(request.param))
    yield request.param
    print("\nfixture finalization: {}".format(request.param))

def test(resource):
    print("\nexecuting test case for {}".format(resource))



