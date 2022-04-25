import pytest
from _pytest.python_api import approx, raises


class TestTino:
    def test_one(self):
        assert True

    def test_two(self):
        assert True

    def not_a_test(self):
        assert True


class MyTestTino:
    def test_three(self):
        assert True


    def test_four(self):
        assert True


# Approx
def test_five():
    value = 0.1 + 0.2
    assert value == approx(0.3)


# Dealing with exceptions with "raises"
def raises_value_exception():
    pass
    raise  ValueError


def test_exception():
    with raises(ValueError):
        raises_value_exception()