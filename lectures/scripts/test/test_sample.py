import pytest

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_add_mirror():
    assert add(5, 2) == add(2, 5)

def test_subtract_mirror():
    assert not (subtract(5, 2) == subtract(2, 5))

def test_add_typ_error():
    with pytest.raises(TypeError):
        add('2', 3)