"""In this file, we will define divers functions that will cover some mathematical operations"""

import math as m


def add(a, b):
    """Add two numbers"""
    return a + b


def calculate_active_and_reactive_power_from_apparent_power_and_power_factor(s, cos_phi):
    """Calculate active and reactive power from apparent power and power factor cos(phi)"""
    p = round(100*s * cos_phi, 2)
    q = round(s * m.sin(m.acos(cos_phi)), 2)

    print(f"Apparent Power: S = {s} MVA")
    print(f"Power Factor: cos(\u03C6) = {cos_phi} ")
    print(f"Active Power: P = {p} MW")
    print(f"Reactive Power: Q = {q} MVar")
    return p, q


def calculate_rated_current_and_pickup_current_from_rated_apparent_power_and_rated_voltage(s_R, u_R, u_k):
    """Calculate rated current, pickup current and short-circuit impedance from a transformator from apparent power and rated voltage"""
    #s_R ... rated apparent power [MVA]
    #u_R ... rated voltage [kV]
    #u_k ... impedance voltage at rated current [%]
    #i_R ... rated current [A]
    #i_pick ... pickup current [A]
    #z_k ... short-circuit impedance [Ohm]
    i_R = round((s_R*10**6)/(m.sqrt(3)*u_R*10**3), 2) #s=sqrt(3)*u_N*i_R
    i_pick = round(1.4*i_R, 2)
    z_k = round((u_k/100)*((u_R*10**3)**2)/(s_R*10**6), 2)

    print("--------------------------------------------------------")
    print(f"apparent power: S_R = {s_R} MVA")
    print(f"rated voltage: U_R = {u_R} kV")
    print(f"impedance voltage at rated current: u_k = {u_k} %")
    print(f"rated current: I_R = {i_R} A")
    print(f"pickup current: I_pick = {i_pick} A")
    print(f"short-circuit impedance: Z_k = {z_k} Ohm")
    print("--------------------------------------------------------")

    return i_R, i_pick, z_k
