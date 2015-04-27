# -*- coding: utf-8 -*-
"""
Physics 177
Lab Assignment 3, exercise 1b
Magnitude of Electric Field in between two point charges
@author: Jeff Kuo
SID: 860884131
"""
#Initialization
import numpy as np
import matplotlib.pylab as plt
import math

############################
#Definition of Constants
############################
pi = 3.14159        #pi, the circular constant
e0 = 8.854187817e-12    #epsilon, the electric constant

############################
# Definition of Variables
############################
q1 = 0.0        #point charge 1
q2 = 0.0        #point charge 2
d  = 0.0        #distance in between the point charges
sp = 0.0        #radius space points for visualization

############################
# User Inputs
############################
"""
print " "
q1 = float(input("Enter point charge 1 (left): "))
print "q1 =", q1, "C"
q2 = float(input("Enter point charge 2 (right): "))
print "q2 =", q2, "C"

d  = float(input("Enter distance (in meters) in between q1 and q2: "))
print "D = ", d, "m"

sp  = float(input("Enter distance in between space points for visualization: "))
"""
###########################
# Default settings
###########################
q1 = 1.
q2 = -1.
d = 10.      #distance in between the point charges in cm

ax = plt.subplot(111)
size = 1. * 100. #Size of the picture in cm
npixel = 200
dx = size / float(npixel)

#Position for the point charges
x1p = (size - d) / 2.
y1p = size / 2.
x2p = (size + d) / 2.
y2p = size / 2.

matrix1 = np.zeros(shape = (npixel,npixel)).astype('float')
matrix2 = np.zeros(shape = (npixel,npixel)).astype('float')

#Matricies for plotting
matrixP1 = np.zeros(shape = (npixel,npixel)).astype('float')
matrixP2 = np.zeros(shape = (npixel,npixel)).astype('float')
matrixP  = np.zeros(shape = (npixel,npixel)).astype('float')
matrixD  = np.zeros(shape = (npixel,npixel)).astype('float')

#vector array
vector = np.zeros(2)

############################
# Defining function phi and its 'constants'
############################
def r1(x,y):
    return np.sqrt((x - x1p)**2 + (y - y2p)**2)
    
def r2(x,y):
    return np.sqrt((x - x2p)**2 + (y - y2p)**2)

def phi(r):
    return ((1. / (4. * pi * e0)) * (q / r))

############################
# Electric Potential Calculation
############################
for j in range(npixel):
    y = float(j) * dx
    for i in range(npixel):
        x = float(i) * dx
        #First Point Charge
        q = q1
        if (r1(x,y) == 0):
            r = 1.e-10
        else:
            r = r1(x,y)
        ep1 = phi(r)
        
        matrix1[j,i] = ep1
                
        #Second Point Charge
        q = q2
        
        if (r2(x,y) == 0):
            r = 1.e-10
        
        else:
            r = r2(x,y)
        ep2 = phi(r)
        
        matrix2[j,i] = ep2

matrix = matrix1 + matrix2

#Numerical derivatives
matrixP = np.gradient(matrix)
matrixP1 = matrixP[0]
matrixP2 = matrixP[1]

for j in range(npixel):
    for i in range(npixel):
        matrixD[j,i] = np.sqrt((matrixP1[j,i])**2 + (matrixP2[j,i]**2))
        
"""
print np.min(matrixD)
print np.max(matrixD)
"""

matrixD = np.log10(matrixD)
"""
print np.min(matrixD)
print np.max(matrixD)
print matrixD[npixel/2,:]
"""
############################
# Plotting 
############################
plt.imshow(matrixD, origin='lower', extent = [0, size, 0, size], vmin=5, vmax=10)
plt.colorbar()

ax.set_title('Log Graph of Electric Field Magnitude')
ax.set_xlabel('x [cm]')
ax.set_ylabel('y [cm]')