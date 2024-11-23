from main import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1, 1) == 2
    assert add(10, 20) == 30
    assert add(23, 32) == 55
    assert add(3, 4) == 7
