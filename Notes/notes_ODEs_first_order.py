import math
import matplotlib.pyplot as plt
import numpy as np

def f(x, t):
    return-x**3 + math.sin(t)
    
# RK2 ================================
a = 0.0         # starting value of t
b = 10.0        # ending value of t
N = 50          # number of steps
h = (b - a)/N   # step size
x = 0.0         # initial condition for x

tpoints = np.arange(a,b,h)
xpoints = []
for t in tpoints:
    xpoints.append(x)
    k1 = h * f(x, t)
    k2 = h * f(x + 0.5 * k1, t + 0.5 * h)
    x += k2
    
plt.figure(dpi=200) # NOTE ADOPTION OF EULER PLOT DETAILS
plt.plot(tpoints, xpoints, 'y-')
plt.xlabel('t')
plt.ylabel('x(t)')
# END RK2  ===========================

# RK4 ================================
a = 0.0
b = 10.0
N = 20     # RK4 with 20 points is about as good as Euler with 1000!
h = (b-a)/N
x = 0.0

tpoints = np.arange(a,b,h)
xpoints = []

for t in tpoints:
    xpoints.append(x)
    k1 = h * f(x, t)
    k2 = h * f(x + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(x + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(x + k3, t + h)
    x += (k1 + 2 * k2 + 2 * k3 + k4)/6
    
plt.plot(tpoints, xpoints, 'g:', lw=2)
plt.show()



print("Coupled ODEs")
def f (r, t):
    # r is a 2D array, so first pull out the vals
    x, y = r[0], r[1]
    fx = x * y - x
    fy = y - x * y + np.sin(t)**2
    return np.array([fx, fy], float)

a = 0.0
b = 10.0
N = 1000
h = (b - a)/N

tpoints = np.arange(a, b, h)
xpoints = []
ypoints = []

# set up array with initial values x0, y0
r = np.array([1.0, 1.0], float)

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    # Below we've just changed `x` into `r`
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4)/6

plt.figure(dpi=200)
plt.plot(tpoints, xpoints, 'k-', label='x')
plt.plot(tpoints, ypoints, 'b--', label='y')
plt.xlabel('t')
plt.legend(loc='best')
plt.show()



print("Lorenz Equation Example")
def f(r, t):
    x, y, z = r[0], r[1], r[2]
    fx = sigma * (y - x)
    fy = R * x - y - x * z
    fz = x * y - B * z
    return np.array([fx, fy, fz], float)

a = 0.0
b = 50.0
N = 5000
h = (b - a)/N
sigma = 10
# use R and B for parameters to differentiate from r and b in this code
R = 28
B = 8 / 3

tpoints = np.arange(a, b, h)
xpoints = []
ypoints = []
zpoints = []
r = np.array([0.0, 1.0, 0.0], float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4)/6

plt.figure(figsize=(8, 3), dpi=200)
plt.subplot(121)
plt.plot(tpoints, ypoints, 'r-')
plt.xlabel('t')
plt.ylabel('y(t)')

plt.subplot(122)
plt.plot(zpoints, xpoints, 'b-')
plt.xlabel('z')
plt.ylabel('x')
plt.show()



print("Voltage Output Example")
def perform_loop(RC):
    """Put the function, f, and the RK4 analysis all in one function.
    This way we can call this outer function once per trial!"""
    
    def f(v_out,t):
        if math.floor(2 * t)%2 == 0:
            v_in = 1
        else:
            v_in = -1
        return (1/(RC)) * (v_in - v_out)
    
    x = 0.0
    xpoints = []
    
    for t in tpoints:
        xpoints.append(x)
        k1 = h * f(x, t)
        k2 = h * f(x + 0.5 * k1, t + 0.5 * h)
        k3 = h * f(x + 0.5 * k2, t + 0.5 * h)
        k4 = h * f(x + k3, t + h)
        x += (k1 + 2 * k2 + 2 * k3 + k4)/6
        
    return xpoints

# Parameters
a = 0.0
b = 3.0
N = 1000
h = (b - a)/N

# Set time values, acquire waveform of the actual pulse
tpoints = np.arange(a, b, h)
V_in = []

for t in tpoints:
    if math.floor(2 * t)%2 == 0:
        V_in.append(1)
    else: V_in.append(-1)
    
# Make figure with three trials
plt.figure(dpi=200)
plt.plot(tpoints, perform_loop(0.01), 'r:', lw=2, label='RC=0.01')
plt.plot(tpoints, perform_loop(0.5), 'g-.', lw=2, label='RC=0.1')
plt.plot(tpoints, perform_loop(5.0), 'b--', lw=2, label='RC=5')
plt.plot(tpoints, V_in, '0.5')
plt.xlabel('t')
plt.ylabel('V_out')
plt.legend(loc='best')
plt.ylim(-1.1, 1.1)
plt.show()