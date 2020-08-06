import pytest

# this test case will not be executed because of mark
@pytest.mark.skip("do not run this for now")
def test_currently_cannot_be_run():
    print("\n\n\nexecuting test")
    assert False
