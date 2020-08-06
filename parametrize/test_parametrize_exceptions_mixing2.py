import pytest
from contextlib import nullcontext as does_not_throw

def method(a):
    if a < 0:
        raise NotImplementedError()
    elif a == 42:
        return True
    elif a > 0:
        raise ValueError()
    else:
        raise RuntimeError()

@pytest.mark.parametrize("a, exc", [
    (-1, pytest.raises(NotImplementedError)),
    (1, pytest.raises(ValueError)),
    (0, pytest.raises(RuntimeError)),
    (42, does_not_throw()),
])
def test_all_of_them(a, exc):
    with exc:
        method(a)
