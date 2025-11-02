# предварительно pip install pytest

from calculator import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_sub():
    assert sub(5, 2) == 3
    assert sub(2, 5) == -3
    assert sub(0, 0) == 0

def test_mul():
    assert mul(3, 4) == 12
    assert mul(-2, 3) == -6
    assert mul(0, 5) == 0

def test_div():
    assert div(6, 2) == 3
    assert div(5, 2) == 2.5
    assert div(0, 3) == 0
    assert div(3, 0) == 'Деление на ноль невозможно!'