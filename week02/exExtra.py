# -*- coding: utf-8 -*-
"""
Physics 177
Lab Assignment 2, exercise Extra
Integration with Romberg's Integration Technique
@author: Jeff Kuo
SID: 860884131
"""

#Initialization
import numpy as np
from scipy import integrate

#function
def f(x):
    return (np.sin(np.sqrt(100. * x)))**2

#Definition
i = 0           #dummy counter for Romberg's
C = 1           #dummy counter for Matrix

accuracy = 0     #integer for accuracy decimal place    
N  = 1           #number of slices
I1 = 0.0         #trapezoidal integral
I2 = 0.0         #second part of adaptive integral
I  = 0.0         #final integral (I = 0.5*I1 + I2)
E  = 0.0         #error (E = (1./3.)*(I - I1))
CI = 0.0         #corrected integral (I - E)

Ra = 0.0         #Romberg's Technique, first integral
Rb = 0.0         #Romberg's Technique, second integral
R  = 0.0         #Romberg's Technique, Next integral
matrixR = np.zeros((10,10)) #Matrix for Romberg's Technique

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
"""
a = 0
b = 1
"""
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
    I = 0.0         #final integral (I = 0.5*I1 + I2)
    E = 0.0         #error (E = (1./3.)*(I - I1))
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
    
    N = N / 2
    
    #Romberg's Technique
    if (C < 2):    
        matrixR[C-1,0] = I1
    matrixR[C,0] = I
    if (C > 1):
        i = 0
        while (i < (C-1)):
            matrixR[C-1,i+1] = matrixR[C-1,i]
            matrixR[C-1,i+1] += (1./(4.**(i+1)-1.))*(matrixR[C-1,i]-matrixR[C-2,i])
            i = i + 1
    

    """
    #For debug use
    print 'Regular Trapezoidal: ', I1
    print 'Adaptive Trapezoidal: ', I
    print 'Error: ', E
    print 'Corrected Result: between', CI
    """
    
    """#Original Trapezoid tests
    comparisonI = int(I * (10**(accuracy)) + 0.5 )
    comparisonC = int(CI* (10**(accuracy)) + 0.5 )
    """
    
    #Romberg's Technique tests
    if (N>1):
        comparisonI = int(matrixR[C-1,C-2] * (10**(accuracy+2)))
        comparisonC = int(matrixR[C-1,C-1] * (10**(accuracy+2)))  
    
    if (comparisonI != comparisonC):
        N = N * 2
        C = C + 1
    
print matrixR    
print "Target accuracy reached at N =", N + 1, "slices."
print 'Rombergs Technique second last term: ', matrixR[C-1,C-2]
print 'Rombergs Technique last term: ', matrixR[C-1,C-1]

"""
print 'Error: ', E
print 'Corrected Integral Result: ', CI
"""
"""
Note:
N is roughly 1900 - 2000 for 6th decimal place estimation with
    adaptive trapezoidal rule
"""
y_n = "N"

print ' '
y_n = raw_input("Would you like to check it with scipy's Romberg result? Y or N: ")
while ((y_n != "Y") and (y_n != "N")):
    print "Please make sure to enter only 'Y' or 'N' without the quotes!"
    y_n = raw_input("Would you like to check it with scipy's Romberg result? Y or N: ")

#Romberg's Integration Technique by scipy
if (y_n == 'Y'):
    result = integrate.romberg(f, a, b, tol=10**(-accuracy), rtol=10**(-accuracy), show = True)