import pytest

def test_skip():
    # code before `pytest.skip` will be executed, and any failure will
    # cause the test to be marked as failed, not skip

    # abort test execution and mark test as skipped
    pytest.skip("Cannot execute this test today")

    # code after `pytest.skip` call will be not be executed
