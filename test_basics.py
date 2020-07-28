import pytest

def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output