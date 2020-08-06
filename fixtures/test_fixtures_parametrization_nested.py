import pytest

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    yield request.param

@pytest.fixture(params=["server1", "server2"])
def server(browser, request):
    yield browser + " on " + request.param

def test(server):
    print("\nexecuting test case for {}".format(server))



