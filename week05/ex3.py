# -*- coding: utf-8 -*-
"""
Physics 177
Lab Assignment 5, exercise 3
Sunspots cycle 
@author: Jeff Kuo
SID: 860884131
"""
import numpy as np
from numpy.fft import rfft,irfft
import matplotlib.pyplot as plt

#######################
# 3a
#######################
#Import Sunspot Data
data = np.genfromtxt('sunspots.txt')
time = data[:,][:,0]        #in months
sunspots = data[:,][:,1]    #number of sunspots

#Plotting the data
plt.subplot(2,1,1)
plt.plot(time,sunspots)

plt.title("Sunspots as a function of Time")
plt.ylabel("Sunspots")
plt.xlabel("Time in Months (since Jan. 1749)")

"""Approximately 130 months per cycle"""

#######################
# 3b & c
#######################
sp_fft = rfft(sunspots)
nc = len(sp_fft)

plt.subplot(2,1,2)
plt.plot(np.arange(nc),np.abs(sp_fft)**2)

plt.title("Full power spectrum")
plt.ylabel("frequency")
plt.xlabel("$|c_k|^2$")

"""Peaks out at |c_k|^2 = 24 where k = 2.014e9"""

#Frequency
k = 2.014e-9

#conversion from seconds to months
k_new = (1 / k) / 60. / 60. / 24. / 30.5
print "Approximately", k_new, "months per cycle."