import pytest

def test_xfail():
    # code before `pytest.xfail` will be executed, and any failure will
    # cause the test to be marked as failed, not xfail

    # abort test execution and mark test as xfail
    pytest.xfail("This test has failed, but we were expecting it to do that")

    # code after `pytest.xfail` call will be not be executed
