import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(x, t):
    return -x**3 + math.sin(t)

x0 = 0
tpoints = np.linspace(0, 10, 1000)

xpoints = odeint(f, x0, tpoints)

plt.figure(dpi = 200)
plt.plot(tpoints, xpoints)
plt.xlabel("time")
plt.ylabel("x")
plt.show()



def f(r, t, omega):
    x, y = r[0], r[1]
    fx = x * y - x
    fy = y - x * y + math.sin(omega * t)**2
    return fx, fy

# define initial conditions and time points
r = [1.0, 1.0]
tpoints = np.linspace(0, 10, 1000)
omega = 1.0

# use odeint
# note that we pass the extra arguments to function f
rpoints = odeint(f, r, tpoints, args = (omega, ))

# rpoint is an array, so pull out xpoints and ypoints
xpoints = rpoints[:,0]
ypoints = rpoints[:,1]

plt.figure(dpi = 200)
plt.plot(tpoints, xpoints, label = "x")
plt.plot(tpoints, ypoints, label = "y")
plt.xlabel("time")
plt.legend(loc = "best")
plt.show()



print("Pendulum")
def f(r, t):
    g, L = 9.8, 0.1
    theta, omega = r[0], r[1]
    ftheta = omega
    fomega = (-g / L) * math.sin(theta)
    return ftheta, fomega

r = [0.99 * math.pi, 0.0]
tpoints = np.linspace(0, 3, 10000)

rpoints = odeint(f, r, tpoints)
thetapoints = rpoints[:,0]
omegapoints = rpoints[:,1]

plt.figure(dpi = 200)
plt.plot(tpoints, thetapoints)
plt.xlabel("Time (s)")
plt.ylabel("Angular Position (rad)")
plt.show()



print("Lotka-Volterra Population Equation")

B = 0.5
C = 0.5
D = 2

def f(r, t, A):
    x, y = r[0], r[1]
    fx = A*x - B*x*y
    fy = C*x*y - D*y
    return fx, fy

def perform_loop(A):
    r = [2.0, 2.0]
    rpoints = odeint(f, r, tpoints, args=(A,))
    return rpoints[:,0], rpoints[:,1], max(rpoints[:,1])

tpoints = np.linspace(0, 20, 1000)
max_preds = []

plt.figure(dpi = 200)
plt.subplot(211)
trial1_prey, trial1_pred, max_pred = perform_loop(1)
max_preds.append(max_pred)
plt.plot(tpoints, trial1_prey, label="Prey")
plt.plot(tpoints, trial1_pred, label="Predators")
plt.legend(loc = "best")
plt.xlabel("Population")
plt.ylabel("Time")

plt.subplot(212)
trial2_prey, trial2_pred, max_pred = perform_loop(1.5)
max_preds.append(max_pred)
trial3_prey, trial3_pred, max_pred = perform_loop(1.8)
max_preds.append(max_pred)
trial4_prey, trial4_pred, max_pred = perform_loop(2.1)
max_preds.append(max_pred)
plt.plot(trial1_prey, trial1_pred, label="1.0")
plt.plot(trial2_prey, trial2_pred, label="1.5")
plt.plot(trial3_prey, trial3_pred, label="1.8")
plt.plot(trial4_prey, trial4_pred, label="2.1")

plt.legend(loc = "best")
plt.xlabel("Predators")
plt.ylabel("Prey")

plt.subplots_adjust(hspace=0.35)
plt.show()

plt.figure(dpi = 200)
plt.plot([1.0, 1.5, 1.8, 2.1], max_preds, "bs--")
plt.xlabel("A")
plt.ylabel("Max # of Predators")
plt.show()