# HW 10-2
# Alec Barker

import matplotlib.pyplot as plt
import numpy as np

fft = np.fft

y = np.loadtxt("Data Files\dow.txt", float)

c = fft.rfft(y)
clow = c.copy()
chigh = c.copy()
cmag = c.copy()

kmax = 100
kmin = 100
maxval = max(c)

for k in range(len(c)):
    if k > kmax:
        clow[k] = 0
    if k < kmin:
        chigh[k] = 0
    if abs(c[k]) < .005 * maxval:
        cmag[k] = 0

y2 = fft.irfft(clow)
y3 = fft.irfft(chigh)
y4 = fft.irfft(cmag)

plt.figure(figsize = (20, 5))
plt.subplots_adjust(hspace=.33,wspace=.27)

# raw data
plt.subplot(241)
plt.plot(y)
plt.xlabel("Time")
plt.ylabel("Signal")
plt.title("Original")

# filtered dft
plt.subplot(245)
plt.semilogy(abs(c))
plt.xlabel("Fourier Coefficients (freq)")
plt.ylabel("Magnitude")

# cleaned up data via inverse dft
plt.subplot(242)
plt.plot(y2.real)
plt.xlabel("Time")
plt.subplots_adjust(hspace=0.6)
plt.title("Low Pass")

# filtered dft
plt.subplot(246)
plt.semilogy(abs(clow))
plt.xlabel("Fourier Coefficients (freq)")

# cleaned up data via inverse dft
plt.subplot(243)
plt.plot(y3.real)
plt.xlabel("Time")
plt.subplots_adjust(hspace=0.6)
plt.title("High Pass")

# filtered dft
plt.subplot(247)
plt.semilogy(abs(chigh))
plt.xlabel("Fourier Coefficients (freq)")

# cleaned up data via inverse dft
plt.subplot(244)
plt.plot(y4.real)
plt.xlabel("Time")
plt.subplots_adjust(hspace=0.6)
plt.title("Magnitude")

# filtered dft
plt.subplot(248)
plt.semilogy(abs(cmag))
plt.xlabel("Fourier Coefficients (freq)")

plt.show()