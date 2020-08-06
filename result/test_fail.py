import pytest

def test_fail():
    # code before `pytest.fail` will be executed and will the
    # test result will be marked as succcess if the method
    # returns before reaching `pytest.fail`

    # abort test execution and mark test as failed
    pytest.fail("This test is failing")

    # code after `pytest.fail` call will be not be executed
