# -*- coding: utf-8 -*-
"""
Physics 177
Lab Assignment 2, exercise 1
Integration with Trapezoidal/Simpson's rule
@author: Jeff Kuo
SID: 860884131
"""

#Initialization
import numpy as np
import matplotlib.pyplot as plt

#Input
counter = 0 #Dummy integer

plotPts = int(input('Enter the amount of plots (Integer): '))
while (plotPts == 0):
    print 'Please make sure the amount of plots is non-zero'
    plotPts = int(input('Enter the amount of plots (Integer): '))


N = plotPts - 1 #Number of slices
arrayX = np.zeros(plotPts)
arrayY = np.zeros(plotPts)

print 'Please make sure the plots go in the order from the lowest to highest'

while (counter < plotPts):
    arrayX[counter] = input('Enter X%s value: ' %(counter + 1)) 
    arrayY[counter] = input('Enter Y%s value: ' %(counter + 1))
    counter = counter + 1
    
print 'x values: ', arrayX
print 'y values: ', arrayY

#Defining Variables, Integers, and dummy objects
a = float(arrayX[0])
b = float(arrayX[N])
height = ( b - a ) / float(N)
TI = 0.0
SI = 0.0
print ' '
"""
                     #Approximating Displacement
"""
TIX = 0.0
SIX = 0.0

#Trapezoidal
counter = 0
while (counter < N):
    base = ( arrayY[counter] + arrayY[counter + 1] )
    area = ( base * height ) / 2.
    TIX += area
    counter += 1

print 'Approximate Integral (Trapezoidal): ', TIX

#Simpson's Rule
if ((N % 2 == 0) & (N > 0)):
    if (N >= 2):
        counter = 0
        while (counter < N-1):
            area=(arrayY[counter]+4.*arrayY[counter+1]+arrayY[counter+2])
            area*=((1./3.)*height)
            SIX += area
            counter += 2
        print 'Approximate Integral (Simpsons): ', SIX
        print ' '
            
    else:
        print 'Insufficient amount of N to complete Simpsons Rule integral.'
else:
    print 'Requires an even amount of slices (N) for Simpsons Rule to operate.'
    print 'Please enter an odd amount of plots'