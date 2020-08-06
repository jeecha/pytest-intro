import pytest

def test_pass():
    # this will pass, as the expected exception class
    # matches the exception thrown
    with pytest.raises(ValueError):
        raise ValueError()

def test_fail():
    # this will fail, as the expected exception was not raised
    with pytest.raises(ValueError):
        pass
