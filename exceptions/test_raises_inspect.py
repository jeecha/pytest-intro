import pytest

def test_raises():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("bad value")
    
    # we can inspect the exception information collected
    # by `pytest.raises` to do some checking
    assert str(exc_info.value) == "bad value"

# our own exception class, that has an extra `errcode` attribute
class MyException(Exception):
    def __init__(self, errmsg, errcode):
        super().__init__(errmsg)
        self.errcode = errcode

def test_raises_custom_exception():
    with pytest.raises(MyException) as exc_info:
        raise MyException("something bad happened", 42)
    
    # we have access to the exception information and can
    # inspect the exception attributes specific to the exception
    # class we were expecting, in this case errcode
    assert exc_info.value.errcode == 42
