import pytest

# this test case will execute and the failure is the
# expected behaviour
@pytest.mark.xfail
def test_where_failure_is_a_success():
    assert True
