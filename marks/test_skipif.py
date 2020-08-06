import pytest
import sys

# this test case will be only executed when running on
# Windows environment
@pytest.mark.skipif(sys.platform == "win32", reason="this test case only runs on Windows")
def test_currently_cannot_be_run():
    print("\n\n\nexecuting test")
    assert False
