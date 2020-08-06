import pytest

class Argument:
    def __init__(self, a, b, expected):
        self.a = a
        self.b = b
        self.expected = expected

def sum(a, b):
    return a + b

def generate_id_for_argument(arg):
    return "{}plus{}equals{}".format(arg.a, arg.b, arg.expected)

@pytest.mark.parametrize("arg", [
    Argument(2, 5, 7), Argument(10, 20, 30)
], ids=generate_id_for_argument)
def test(arg):
    assert sum(arg.a, arg.b) == arg.expected

