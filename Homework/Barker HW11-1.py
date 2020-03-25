# HW 11-1
# Alec Barker

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint

"""
H = Hyperion
S = Saturn
a = axis
e = eccentricity
P = periapsis
SH = r = distance from Saturn to Hyperion
SP = distance from Saturn to periapsis
phi = orbital angle from line SP to line SH
theta = smallest principal moment of inertia/longest axis of the moon
omega = rate that Hyperion orbits Saturn
"""
e = 0.1
B_minus_A_over_C = 0.265

def f(omega, phi):
    return -1 * B_minus_A_over_C * (3 / (2 * (1 - e**2))) * \
        ((1 + e * math.cos(phi)) / (1 - e**2)) * math.sin(2 * \
        ((-1 * omega * (e**2 + 1)**2) / (1 + e * math.cos(phi))**2 - phi))

phi_points = np.linspace(0, 200, 1000)

omega = 0
omega_points_1 = odeint(f, omega, phi_points)

omega = 2
omega_points_2 = odeint(f, omega, phi_points)

plt.figure(dpi = 200)
plt.subplot(211)
plt.title("Omega = 0", size="xx-large")
plt.plot(phi_points, omega_points_1)
plt.ylabel("Spin Rate Ω")

plt.subplot(212)
plt.title("Omega = 2", size="xx-large")
plt.plot(phi_points, omega_points_2)
plt.ylabel("Spin Rate Ω")
plt.xlabel("Orbital Angle ϕ (Radians)")

plt.tight_layout()
plt.show()