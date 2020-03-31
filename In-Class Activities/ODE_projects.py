import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint

# Project 1
def f_polar(r, t):
    # set params
    B = 1.0
    m = 1.0
    q = 1.0
    E = .05
    r_accel = 0.01 #0
    
    # unpack input
    radius, theta, z, z_velocity = r # can do this instead of `=r[0],r[1],...`
    
    # determine output
    fr = r_accel
    ftheta = -q * B / m
    fz = z_velocity
    fzv = E
    
    return fr, ftheta, fz, fzv

# Initial conditions and odeint
r = [1.0, 0.0, 0.0, 0.0] #r, theta, z, z_velocity
N = int(1E5)
tpoints = np.linspace(0, 50, N)
rpoints = odeint(f_polar, r, tpoints)

# Unpack output of odeint
radius_points = rpoints[:, 0]
theta_points = rpoints[:, 1]
z_points = rpoints[:, 2]

# transform r, theta to x, y
x_points, y_points, zpoints = [], [], []
for i in range(N):
    x_points.append(radius_points[i] * math.cos(theta_points[i]))
    y_points.append(radius_points[i] * math.sin(theta_points[i]))

# Make our plots
fig = plt.figure(dpi=200)

# 2D plot
ax = fig.add_subplot(111)
ax.plot(x_points, y_points)
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

# 3D plot
fig = plt.figure(dpi=200)
ax = fig.gca(projection='3d')
ax.plot(x_points, y_points, z_points)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()



# Problem 2
def central_force(r,t):
    # set parameters
    G = 1
    m1 = 1
    m2 = 1
    # unpack input
    x1, y1, x2, y2, vx1, vy1, vx2, vy2 = r
    
    # determine distance
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    # if d is very small, stop the motion (collision)
    if d < 0.02:
        return 0, 0, 0, 0, 0, 0, 0, 0
    
    # determine angle
    theta = math.atan(abs((y2 - y1) / (x2 - x1)))
    # set output
    fx1 = vx1
    fy1 = vy1
    
    fx2 = vx2
    fy2 = vy2
    
    fvx1 = (G * m2 / (d**2)) * math.cos(theta)
    fvy1 = (G * m2 / (d**2)) * math.sin(theta)
    
    fvx2 = (G * m1 / (d**2)) * math.cos(theta)
    fvy2 = (G * m2 / (d**2)) * math.sin(theta)
    
    # we have to be careful about the directions of these forces...
    if x2 >= x1 and y2 >= y1:
        # m2 is in Q1 relative to m1
        # forces on m1 are positive; forces on m2 are negative
        fvx2 *= -1
        fvy2 *= -1
    elif x2 >= x1 and y2 < y1:
        # m2 is in Q4 relative to m1
        fvy1 *= -1
        fvx2 *= -1
    elif x2 < x1 and y2 >= y1:
        #m2 is in Q2 relative to m1
        fvx1 *= -1
        fvy2 *= -1
    else:
        #m2 is in Q3 relative to m1
        fvx1 *= -1
        fvy1 *= -1
    
    return fx1, fy1, fx2, fy2, fvx1, fvy1, fvx2, fvy2

# Initial conditions and odeint
# case 1 (separated along x axis, no velocity):
#r = [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# case 2 (m1 is at the origin, m2 is at 1,1; Initial...
# ...velocities are in the +x and -x directions, respectively)
r = [0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, -0.5]

tpoints = np.linspace(0, 6, int(1E5))
rpoints = odeint(central_force, r, tpoints)

m1_x = rpoints[:, 0]
m1_y = rpoints[:, 1]
m2_x = rpoints[:, 2]
m2_y = rpoints[:, 3]

plt.figure(dpi=200)
plt.plot(m1_x, m1_y, 'g-')
plt.plot(m2_x, m2_y, 'r-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 3D plot
fig = plt.figure(dpi=200)
ax = fig.gca(projection='3d')
ax.plot(m1_x, m1_y, tpoints,'g-')
ax.plot(m2_x, m2_y, tpoints,'r-')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('t')
plt.show()