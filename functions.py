"""In this file, we will define divers functions that will cover some mathematical operations"""

import math as m


def add(a, b):
    """Add two numbers"""
    return a + b


def calculate_active_and_reactive_power_from_apparent_power_and_power_factor(s, cos_phi):
    """Calculate active and reactive power from apparent power and power factor cos(phi)"""
    p = s * cos_phi
    q = s * m.sin(m.acos(cos_phi))

    print(f"Apparent Power: S = {s} MVA")
    print(f"Power Factor: cos(\u03C6) = {cos_phi} ")
    print(f"Active Power: P = {p} MW")
    print(f"Reactive Power: Q = {q} MVar")
    return p, q
