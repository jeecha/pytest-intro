import pytest
from contextlib import nullcontext as does_not_throw

def calculator(operation, a, b):
    if operation == "sum":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        raise ValueError("unknown operation")

@pytest.mark.parametrize("operation, a, b, result, exc", [
    ("sum", 1, 2, 3, does_not_throw()),
    ("sub", 10, 1, 9, does_not_throw()),
    ("mul", 10, 10, 100, does_not_throw()),
    ("div", 10, 5, 2, does_not_throw()),
    ("div", 10, 0, None, pytest.raises(ZeroDivisionError)),
    ("unkknownoperation", 1, 1, None, pytest.raises(ValueError)),
])
def test_all(operation, a, b, result, exc):
    with exc:
        assert calculator(operation, a, b) == result
