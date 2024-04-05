"""In this file, we will define divers functions that will cover some mathematical operations"""

import math as m


def add(a, b):
    """Add two numbers"""
    return a + b


def calculate_active_and_reactive_power_from_apparent_power_and_power_factor(s, cos_phi):
    """Calculate active and reactive power from apparent power and power factor cos(phi)"""
    while(abs(cos_phi) > 1):  #As long as the power factor is greater than one, ask for a new input
        cos_phi = float(input(
            'The power factor is greater than one. The Power Factor has to be between -1 and 1. Therefore, please enter a number between -1 and 1:'))
    p = round(s * cos_phi, 2)
    q = round(s * m.sin(m.acos(cos_phi)), 2)

    print(f"Apparent Power: S = {s} MVA")
    print(f"Power Factor: cos(\u03C6) = {cos_phi} ")
    print(f"Active Power: P = {p} MW")
    print(f"Reactive Power: Q = {q} MVar")
    return p, q
