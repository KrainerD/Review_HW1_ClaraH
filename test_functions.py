"""This file tests the functions in functions.py"""

from functions import add
from functions import calculate_active_and_reactive_power_from_apparent_power_and_power_factor


def test_add():
    assert add(1, 2) == 3
    assert add(0, 3) == 3
    assert add(3, -2) == 1
    assert add(200, 50) == 250


def test_calculate_active_and_reactive_power_from_apparent_power_and_power_factor():
    assert calculate_active_and_reactive_power_from_apparent_power_and_power_factor(3, 1)[0] == 3
    assert calculate_active_and_reactive_power_from_apparent_power_and_power_factor(3, 1)[1] == 0
    assert calculate_active_and_reactive_power_from_apparent_power_and_power_factor(3, 0.9)[0] == 2.7
    assert calculate_active_and_reactive_power_from_apparent_power_and_power_factor(3, 0.9)[1] == 1.31
