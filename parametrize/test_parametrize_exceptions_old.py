import pytest

def method(a):
    if a < 0:
        raise NotImplementedError()
    elif a > 0:
        raise ValueError()
    else:
        raise RuntimeError()

@pytest.mark.parametrize("a, exc", [
    (-1, NotImplementedError),
    (1, ValueError),
    (0, RuntimeError),
])
def test_all_of_them(a, exc):
    with pytest.raises(exc):
        method(a)
