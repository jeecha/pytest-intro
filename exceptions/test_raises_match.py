import pytest

def test_raises():
    # this will pass, as the expected exception class
    # matches the exception thrown
    with pytest.raises(ValueError, match="very bad"):
        raise ValueError("this is very bad")

