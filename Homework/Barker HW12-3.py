# HW 12-3
# Alec Barker

from scipy import integrate
import numpy as np

def f(theta, z, r):
    return z**2 * r**3

H = 2
R = 2.5

value, error = integrate.tplquad(f, 0,R, lambda r: r*H/R,H, 0,2*np.pi)

print("quad() indicates the value is {0:.3e} with absolute error no greater than {1:.3e}".format(value,error))