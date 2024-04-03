"""This file tests the functions in functions.py"""

from functions import add


def test_add():
    assert add(1, 2) == 3
    assert add(0, 3) == 3
    assert add(3, -2) == 1
    assert add(200, 50) == 250
