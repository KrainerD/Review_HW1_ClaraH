"""This file tests the functions in functions.py"""

from functions import add
from functions import calculate_active_and_reactive_power_from_apparent_power_and_power_factor
from functions import calculate_rated_current_and_pickup_current_from_rated_apparent_power_and_rated_voltage


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


def test_calculate_rated_current_and_pickup_current_from_rated_apparent_power_and_rated_voltage():
    t1 = calculate_rated_current_and_pickup_current_from_rated_apparent_power_and_rated_voltage(40, 20, 6)
    assert t1[0] == 1154.7
    assert t1[1] == 1616.58
    assert t1[2] == 0.6
    t2 = calculate_rated_current_and_pickup_current_from_rated_apparent_power_and_rated_voltage(63, 20, 6)
    assert t2[0] == 1818.65
    assert t2[1] == 2546.11
    assert t2[2] == 0.38
