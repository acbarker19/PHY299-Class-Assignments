import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation # Note the new import here
from scipy.integrate import odeint
import math

print("Sin Wave")
# Make a sine curve as a simple example ======================================
xvals = np.linspace(0,6*np.pi,1000)
yvals = np.sin(xvals)

# Make a plot ================================================================
fig = plt.figure(dpi=300) # We -must- give the figure a name
ax = fig.add_subplot(111)
line, = ax.plot([],[],'k-') # Note the comma after `line` to make it a tuple
marker = ax.scatter(0,0,marker='o',s=30,c='g') # Leading dot

# Force the viewing window to account for all of the data
ax.set_xlim(1.1*min(xvals),1.1*max(xvals))
ax.set_ylim(1.1*min(yvals),1.1*max(yvals))
plt.show()

# Define a function that will update our plot ================================
def update(i):
    """
    This function will be called over and over when we make the animation.
    i will cycle through a range of values that we specify.
    For us, i will be an integer that corresponds to how much of our data to
    show.
    """
    line.set_data(xvals[:i],yvals[:i]) # Plot up to index i
    marker.set_offsets([xvals[i],yvals[i]])
    
# Now create the animation ===================================================
"""
'frames' is the thing that is used as the argument for the `update` function.
Here we give an integer 1000, so we move from 0 to 999 in integer steps.
'interval' is the amount of time to let pass between each frame (in
milliseconds)
'repeat_delay' is how long to pause at the end of the animation before
restarting
(in milliseconds)
"""
ani = animation.FuncAnimation(fig, update, frames=1000, interval=20,
                              repeat_delay=300)



print("Lotka Volterra Predator/Prey Dynamics")
# Function Definitions =====================================================

# Function for odeint
def derivs(r,t):
    A = 1.5
    B = 0.5
    C = 0.5
    D = 2
    x,y = r[0],r[1]
    fx = A*x - B*x*y
    fy = C*x*y-D*y
    return fx,fy

# Function for animation
def update(i):
    line_prey.set_data(tpoints[:i],prey[:i])
    line_pred.set_data(tpoints[:i],pred[:i])
    line_phase.set_data(prey[:i],pred[:i])
    marker.set_offsets([prey[i],pred[i]])

# Perform integration ========================================================
r = [2.0,2.0]
tpoints = np.linspace(0,20,1000)
rpoints = odeint(derivs,r,tpoints)

# Separate out values
prey = rpoints[:,0]
pred = rpoints[:,1]

# Make plot ==================================================================
fig = plt.figure()
ax1 = plt.subplot(211)
line_prey, = ax1.plot([],[],'g-',label='prey')
line_pred, = ax1.plot([],[],'r-',label='predator')
ax1.set_xlim(0,20)
ax1.set_ylim(0,10)
ax1.set_xlabel('time')
ax1.set_ylabel('population')
ax1.legend(loc='lower right')

ax2 = plt.subplot(212)
line_phase, = ax2.plot([],[],'k')
marker = ax2.scatter(0,0,marker='o',s=30,c='k')
ax2.set_ylim(0,10)
ax2.set_xlim(0,10)
ax2.set_xlabel('prey')
ax2.set_ylabel('predator')
plt.subplots_adjust(hspace=0.35)
plt.show()
# Make animation =============================================================
ani = animation.FuncAnimation(fig, update, frames=1000, interval=20,
                              repeat_delay=300)



print("Two Body Problem")
def central_force(r,t):
    # set parameters
    G = 1
    m1 = 1
    m2 = 1
    # unpack input
    x1,y1,x2,y2,vx1,vy1,vx2,vy2 = r
    # determine distance
    d = ((x2-x1)**2 + (y2-y1)**2)**.5
    # if d is very small, stop the motion (collision)
    if d < .02:
        return 0,0,0,0,0,0,0,0

    # determine angle
    theta = math.atan(abs((y2-y1)/(x2-x1)))
    
    # set output
    fx1 = vx1
    fy1 = vy1
    fx2 = vx2
    fy2 = vy2
    fvx1 = (G*m2/(d**2))*math.cos(theta)
    fvy1 = (G*m2/(d**2))*math.sin(theta)
    fvx2 = (G*m1/(d**2))*math.cos(theta)
    fvy2 = (G*m1/(d**2))*math.sin(theta)
    
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
    return fx1,fy1,fx2,fy2,fvx1,fvy1,fvx2,fvy2

# (NEW FUNCTION)
def update(i):
    line1.set_data(m1_x[:i],m1_y[:i])
    line2.set_data(m2_x[:i],m2_y[:i])
    marker1.set_offsets([m1_x[i],m1_y[i]])
    marker2.set_offsets([m2_x[i],m2_y[i]])

# Initial conditions and odeint
# Here we just have case 2 (m1 is at the origin, m2 is at 1,1; Initial
# velocities are in the +x and -x directions, respectively)
r = [0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, -0.5]

tpoints = np.linspace(0,6,1000)
rpoints = odeint(central_force,r,tpoints)

m1_x = rpoints[:,0]
m1_y = rpoints[:,1]
m2_x = rpoints[:,2]
m2_y = rpoints[:,3]

# (NEW) MAKE INITIAL FIGURE
fig = plt.figure()
ax = plt.subplot(111)
line1, = ax.plot([],[],'g-')
line2, = ax.plot([],[],'r-')
marker1 = ax.scatter(0,0,marker='o',s=30,c='g')
marker2 = ax.scatter(0,0,marker='o',s=30,c='r')
ax.set_xlim(min([min(m1_x),min(m2_x)]),max([max(m1_x),max(m2_x)])) # This is
    # just to force window size
ax.set_ylim(min([min(m1_y),min(m2_y)]),max([max(m1_y),max(m2_y)])) # This is
    # just to force window size
plt.show()

# (NEW) MAKE ANIMATION (note frames is same as length of `tpoints`)
ani = animation.FuncAnimation(fig, update, frames=1000, interval=20,
                              repeat_delay=300)
