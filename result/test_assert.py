def test_pass():
    # this test well pass, because `1 == 1` -> True
    assert 1 == 1

def test_fail():
    # this test will fail, because `1 != 1` -> False
    assert 1 != 1

def test_containers():
    a = [1, 2, 3]
    # fail, if the container is emtpy
    assert a
    # fail, if element is not in container
    assert 2 in a

