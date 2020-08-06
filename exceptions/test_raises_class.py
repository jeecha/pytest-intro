import pytest

def test_pass():
    # this test will pass, because ValueError is descendant of Exception
    with pytest.raises(Exception):
        raise ValueError()

def test_fail():
    # this test will fail, because we were expecting ValueError,
    # but the code threw NotImplementedError
    with pytest.raises(ValueError):
        raise NotImplementedError()
