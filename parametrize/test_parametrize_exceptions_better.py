import pytest

def method(a):
    if a < 0:
        raise NotImplementedError()
    elif a > 0:
        raise ValueError()
    elif a == 42:
        return True
    else:
        raise RuntimeError()

@pytest.mark.parametrize("a, exc", [
    (-1, NotImplementedError),
    (1, ValueError),
    (0, RuntimeError),
    (42, None),
])
def test_all_of_them(a, exc):
    with pytest.raises(exc):
        method(a)
