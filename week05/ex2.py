# -*- coding: utf-8 -*-
"""
Physics 177
Lab Assignment 5, exercise 2
Using Fourier Transformation to calculate the coefficients 
@author: Jeff Kuo
SID: 860884131
"""
#######################
# Initialization
#######################

import numpy as np
from numpy.fft import rfft,irfft
from scipy import signal
import matplotlib.pyplot as plt

#######################
# Functions
#######################

#Square Wave
def sqWv(t):
    return signal.square(2*np.pi*1*t)

#Sawtooth Wave
def stWv(t):
    return signal.sawtooth(2*np.pi*1*t)

#modulated Sine Wave
def modSin(t):
    return np.sin(np.pi * t) * np.sin(20. * np.pi * t)

#N=1000
t = np.linspace(0,1,1000,dtype=float)

#######################
# Fourier Transformation
#######################

coeff1 = rfft(sqWv(t))
coeff2 = rfft(stWv(t))
coeff3 = rfft(modSin(t))

N = np.arange(len(coeff1))

#######################
# Plotting
#######################

ax1 = plt.subplot(321)

#Square Wave
plt.subplot(3,2,1)
plt.plot(t, sqWv(t))

plt.ylim(-1.5,1.5)
plt.xlim(-0.1,1.1)

plt.ylabel("Square Wave")

#Sawtooth Wave
plt.subplot(3,2,3)
plt.plot(t, stWv(t))

plt.ylim(-1.5,1.5)
plt.xlim(-0.1,1.1)

plt.ylabel("Sawtooth Wave")

#Modulated Sine Wave
plt.subplot(3,2,5)
plt.plot(t, modSin(t))

plt.ylim(-1.5,1.5)
plt.xlim(-0.1,1.1)

plt.xlabel("time")
plt.ylabel("Mod. Sine Wave")

#######################
# Plotting Fourier Power Spectrum
#######################
plt.subplot(3,2,2)
plt.plot(N, np.abs(coeff1**2))

plt.subplot(3,2,4)
plt.plot(N, np.abs(coeff2**2))

plt.subplot(3,2,6)
plt.plot(N, np.abs(coeff3**2))
