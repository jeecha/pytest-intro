import pytest

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

@pytest.mark.parametrize("operation, a, b, result", [
    ("sum", 1, 2, 3),
    ("sub", 10, 1, 9),
    ("mul", 10, 10, 100),
    ("div", 10, 5, 2),
])
def test_nothrow(operation, a, b, result):
    assert calculator(operation, a, b) == result

@pytest.mark.parametrize("operation, a, b, exc", [
    ("div", 10, 0, ZeroDivisionError),
    ("unkknownoperation", 1, 1, ValueError),
])
def test_throws(operation, a, b, exc):
    with pytest.raises(exc):
        calculator(operation, a, b)
