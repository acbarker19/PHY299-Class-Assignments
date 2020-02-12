# Data Functions Created by Dr. Colin Campbell
# Graphing Function Created by Alec Barker

"""
In module 7 of the class notes, we looked at the semi-empirical mass formula
for the nuclear binding energy. That module tasked students with developing
3 increasingly-complex functions to ultimately acquire the maximum possible
value of B/A (binding energy / nucleon) for each atomic number Z from 1 to 100.

This script provides a solution to that task. Note that because we ultimately
only care about the output of function #3, we've defined f1 and f3 inside of
f3. This means we can't call f1 and f2 outside of f3, but it makes things 
conceptually easier to follow.
"""

import matplotlib.pyplot as plt

def f3():
    """
    Evaluates the maximum value of B/A for every value of Z from 1 to 100, 
    inclusive.
    
    Note that here we define f1 and f2 inside of f3!
    
    Returns a list of tuples: [(max(B/A),Z), (), ...]
    """
    def f1(a,z):
        """ 
        Determines the binding energy per nucleon given the atomic mass number
        a and the atomic number z, using the semi-empirical mass formula.
        """
        # First define our parameters (in units of MeV)
        a1 = 15.67
        a2 = 17.23
        a3 = 0.75
        a4 = 93.2
        if a%2 == 1:
            a5 = 0.0   # a is odd
        elif z%2 == 0:
            a5 = 12.0  # a and z are even
        else:
            a5 = -12.0 # a is even, z is odd

        # Now compute the binding energy
        b = a1*a - a2*a**(2/3) - a3*(z**2)/(a**(1/3)) - a4*((a-2*z)**2)/a + a5/(a**0.5)

        # provide binding energy per nucleon
        return b/a
    def f2(z):
        """
        Takes an atomic number z and determines
        the maximum value of b/a for a = z to
        a = 3z.
        """
        out = []
        # Make a list of tuples with entries (b/a,a)
        for a in range(z,3*z):
            out.append(f1(a,z))
        # Return the max value of b/a
        return max(out)

    out = []
    # For each value of z, snag the output of f2()
    for z in range(1,101):
        out.append((f2(z),z))
    
    # Return the list of tuples 
    return out

# Acquire our data
data = f3()

def plot():
    yvals, xvals = zip(*data)
    fig = plt.figure(dpi = 200)   # dpi = 300 so the resolution is increased
    plt.plot(xvals, yvals, "m-", marker = "d", lw = 0.5, ms = 3)
    plt.xlabel("Z")
    plt.ylabel("max(B/A) (MeV)")
    plt.title("Semi-Empirical Mass Binding Formula")
    plt.show()
    
plot()