import matplotlib.pyplot as plt
import numpy as np
# cmath can handle j = sqrt(-1)
from cmath import exp

def dft(y):
    N = len(y)
    c = np.zeros(N, complex)
    for k in range(N):
        for n in range(N):
            c[k] += y[n]*exp(-2j*np.pi*k*n/N)
    return c

def idft(c):
    N = len(c)
    y = np.zeros(N, complex)
    for n in range(N):
        for k in range(N):
            y[n] += c[k]*exp(2j*np.pi*k*n/N)
    return y/N

y = np.loadtxt("Data Files\pitch.txt", float)
c = dft(y)

for i in range(len(c)):
    if abs(c[i]) < 30:
        c[i] = 0

y2 = idft(c)

plt.figure(dpi = 250)

# raw data
plt.subplot(311)
plt.plot(y)
plt.xlabel("Time")
plt.ylabel("Signal")

# filtered dft
plt.subplot(312)
plt.plot(abs(c))
plt.xlabel("Fourier Coefficients (freq)")
plt.ylabel("Magnitude")

# cleaned up data via inverse dft
plt.subplot(313)
plt.plot(y2.real)
plt.xlabel("Time")
plt.ylabel("Signal")
plt.subplots_adjust(hspace=0.6)
plt.show()