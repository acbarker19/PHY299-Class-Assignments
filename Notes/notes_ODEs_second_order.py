import math
import matplotlib.pyplot as plt
import numpy as np

def f(r, t):
    x, y = r[0], r[1]
    fx = y     # NEW: define fx and fy
    fy = -k * x
    return np.array([fx, fy], float)

a = 0.0
b = 10.0
N = 1000
h = (b - a)/N
k = 2.0     # NEW: define k

tpoints = np.arange(a, b, h)
xpoints = []
ypoints = []

r = np.array([1.0, 1.0], float)   # NEW: define init. position and velocity

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4)/6
    
plt.figure(dpi = 200)
plt.plot(tpoints, xpoints)
plt.xlabel("t")
plt.ylabel("position")
plt.show()



print("Motion of a Simple Pendulum")
def f(r,t):
    theta, omega = r[0], r[1]
    f_theta = omega
    # f_omega = -(g/L) * np.sin(theta)
    f_omega = -(g/L) * np.sin(theta) + C * np.cos(theta) * np.sin(OMEGA * t)
    return np.array([f_theta, f_omega], float)

a = 0.0
b = 100.0
N = 10000
h = (b - a)/N
g = 9.81
L = 0.1
C = 2
OMEGA = 10.5

tpoints = np.arange(a, b, h)
theta_points = []
omega_points = []

# r = np.array([0.99 * np.pi, 0.0], float) # pt 1
r = np.array([0.0, 0.0], float) # pt 2
for t in tpoints:
    theta_points.append(r[0])
    omega_points.append(r[1])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5* h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4)/6

#SHO
thy = [0.99 * np.pi * np.sin(((g/L)**0.5 * t) + 0.5 * np.pi) for t in tpoints]
plt.figure(dpi=200)
#plt.plot(tpoints, thy, '0.5', label='SHM')
plt.plot(tpoints, theta_points, 'b-', label='Actual')
plt.xlabel('time')
plt.ylabel('angular displacement (rad)')
plt.legend(loc='lower right')
plt.show()



print("Motion of a Pendulum")

def f(r, t):
    theta, omega = r[0], r[1]
    ftheta = omega
    fomega = (-g / L) * math.sin(theta)
    return np.array([ftheta, fomega], float)

a = 0.0
b = 10.0
N = 1000
h = (b - a)/N
k = 2.0
g = 9.81
L = 0.1

tpoints = np.arange(a, b, h)
thetapoints = []
omegapoints = []

r = np.array([0.99 * math.pi, 0.0], float)

for t in tpoints:
    thetapoints.append(r[0])
    omegapoints.append(r[1])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4)/6
    
plt.figure(dpi = 200)

plt.plot(tpoints, thetapoints)
plt.plot(tpoints, omegapoints)
plt.xlabel("t")
plt.ylabel("Angular Displacement")

plt.show()



print("Motion of a Driven Pendulum")

def f(r, t):
    theta, omega = r[0], r[1]
    ftheta = omega
    fomega = (-g / L) * math.sin(theta) + C * math.cos(theta) * math.sin(Omega * t)
    return np.array([ftheta, fomega], float)

a = 0.0
b = 100
N = 10000
h = (b - a)/N
k = 2.0
g = 9.81
L = 0.1
C = 2
Omega = 5

tpoints = np.arange(a, b, h)
thetapoints = []
omegapoints = []

r = np.array([0.0, 0.0], float)

for t in tpoints:
    thetapoints.append(r[0])
    omegapoints.append(r[1])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4)/6
    
plt.figure(dpi = 200)

plt.plot(tpoints, thetapoints)
# plt.plot(tpoints, omegapoints)
plt.xlabel("t")
plt.ylabel("Angular Displacement")

plt.show()