# -*- coding: utf-8 -*-
"""
Physics 177
Lab Assignment 2, exercise 4
Integration with adaptive Trapezoidal rule
@author: Jeff Kuo
SID: 860884131
"""

#Initialization
import numpy as np

#function
def f(x):
    return (np.sin(np.sqrt(100. * x)))**2
    
#Definition
accuracy = 0    #integer for accuracy decimal place    
N = 1           #number of slices
I1 = 0.0        #trapezoidal integral
I2 = 0.0        #second part of adaptive integral
I = 0.0         #final integral (I = 0.5*I1 + I2)
E = 0.0         #error (E = (1./3.)*(I - I1))
CI = 0.0        #corrected integral (I - E)

comparisonI = 0 #integer dummy for comparison
comparisonC = 5 #integer dummy for comparison

#For Future use
"""
N = int(input('Enter the amount of slices: ')) #Slices for integration
if (N == 0):
    while (N == 0):
        print 'The amount of slices cannot be zero!'
        N = int(input('Enter the amount of slices: ')) #Slices for integration
"""

a = float(input('Enter the starting boundry: a = '))
b = float(input('Enter the ending boundry: b = '))

#Expected decimal place for Approximate Accuracy input
print "For accuracy decimal place, it is highly suggested not to exceed 6!"
accuracy =input("Enter the lowest decimal place of the approximate accuracy: ")
if (accuracy <= 0):
    while (accuracy <= 0):
        print "Please make sure it is a positive integer!"
        accuracy = input("Enter the lowest decimal place of the approximate accuracy: ")

accuracy = int(accuracy)

print ' '
print "Calculating outcome, please standby..."
print ' '

while (comparisonI != comparisonC):
    h = float(b - a) / ( float(N) )
    
    #reset the variables
    I1 = 0.0        #trapezoidal integral
    I2 = 0.0        #second part of adaptive integral
    I  = 0.0        #final integral (I = 0.5*I1 + I2)
    E  = 0.0        #error (E = (1./3.)*(I - I1))
    CI = 0.0        #corrected integral (I - E)

    #Integration
    I1 = 0.5*f(a) + 0.5*f(b)
    for k in range(1,N):
        I1 += f(a + k*h)

    I1 = I1 * h
    
    #Second part
    N = N * 2
    h = (b - a) / ( float(N) )

    #Only calculates the odd part of the function, reducing much of the calculation
    #time required for two seperate Trapezoidal integrations
    for k in range(1,N,2):
        I2 += h * f(a + k*h)

    #Addition of the two parts
    I = ((0.5)*I1 + I2)

    #Calculation of Error
    E = (1./3.) * (I - I1)

    #Corrected Result
    CI= I - E
    
    comparisonI = int(I * (10**(accuracy)) + 0.5 )
    comparisonC = int(CI* (10**(accuracy)) + 0.5 )

    """
    #For debug use
    print 'Regular Trapezoidal: ', I1
    print 'Adaptive Trapezoidal: ', I
    print 'Error: ', E
    print 'Corrected Result: between', CI
    """
    
    N = N / 2
    if (comparisonI != comparisonC):
        N = N * 2

    else:
        print "Target accuracy reached at N =", N + 1, "slices."

print 'Regular Trapezoidal = ', I1
print 'Adaptive Trapezoidal = ', I
print 'Error = ', E
print 'Corrected Integral Result = ', CI

"""
Note:
N is roughly 2000 - 2100 for 6th decimal place estimation.
"""