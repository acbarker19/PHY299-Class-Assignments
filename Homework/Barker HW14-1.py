# HW 14-1
# Alec Barker

import matplotlib.pyplot as plt
from scipy import optimize, stats
import numpy as np

def get_temps(file_path):
    file = open(file_path)
    
    all_temps = []

    year_temps = {}
    current_year = 1995
    current_year_temps = []
    
    for line in file:
        line_data = line.split("         ")
        
        line_data[0] = int(line_data[0].strip())
        line_data[1] = int(line_data[1].strip())
        line_data[2] = int(line_data[2].strip())
        line_data[3] = float(line_data[3].strip())
        
        if(line_data[3] > 0):
            all_temps.append(line_data[3])
            
        if line_data[2] != current_year:
            year_temps.update({str(current_year) : current_year_temps})
            current_year = line_data[2]
            current_year_temps = []
        current_year_temps.append(line_data[3])
    
    # Adds data for the last year to the dictionary
    year_temps.update({str(current_year) : current_year_temps})
    
    return all_temps, year_temps

def average(values):
    return sum(values) / len(values)

def f(t, A, B, C, D):
    # sinusoidal fit
    return A*np.sin(B*t+C)+D

def rms(y, yfit):
    # compute the root-mean-square error
    return np.sqrt(np.sum((y-yfit)**2)/len(y))



all_temps, year_temps = get_temps("Data Files/MDBALTIM.txt")

A, B, C, D = 1, 1, 1, 1
xvals = np.linspace(0, len(all_temps), len(all_temps))
yvals = A * np.sin(B * xvals + C) + D + all_temps

# Determine the fit
popt, pcov = optimize.curve_fit(f, xvals, yvals, [3, 0.0171, 5, -2])

# Generate yvals with this fit
y_fit = [f(x, *popt) for x in xvals]

# Report the fit and the error.
print("The best-fit parameters are {0}.\nThis yields a \
RMS error of {1:.2e}".format(popt, rms(yvals, y_fit)))

T_fit = 2*np.pi/popt[1]
print("Optimized period = {0:.2f} days".format(T_fit))
 
plt.figure(dpi=200)

plt.subplot(211)
plt.title("Daily Temperatures From 1995 to 2017")
plt.plot(range(len(all_temps)), all_temps)
plt.ylabel("Temperature")

plt.subplot(212)
plt.scatter(range(len(all_temps)), all_temps, color="g", s=1)
plt.plot(xvals, y_fit, color="k")
plt.xlabel("Days since January 1, 1995")
plt.ylabel("Temperature")

plt.tight_layout()
plt.show()