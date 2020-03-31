# HW 12-2
# Alec Barker

# P8.2.1

from scipy import integrate
import numpy as np

def f(x):
    return np.sqrt(x) * np.sqrt(1 + (0.5 * x**(-0.5))**2)

value, error = integrate.quad(f,0,1)

print("quad() indicates the value is {0:.2e} with absolute error no greater than {1:.2e}".format(value * 2 * np.pi,error * 2 * np.pi))