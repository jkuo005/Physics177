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
matrixR = np.zeros((2,2)) #Matrix for Romberg's Technique
matrixE = np.zeros((2,2)) #Matrix for Romberg's error estimation

matrixDummy = np.zeros((1,1)) #

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

print "For accuracy decimal place, it is highly suggested not to exceed 10!"
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
            matrixE[C-1,i+1] = matrixR[C-1,i+1] - matrixR[C-1,i]
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
    #Calculation of Error for Romberg
    
    
    #Romberg's Technique tests
    """
    if (N>1):
        comparisonI = int(matrixR[C-1,C-2] * (10**(accuracy)) + 0.5)
        comparisonC = int(matrixR[C-1,C-1] * (10**(accuracy)) + 0.5) 
    """
    if (N>1):
        comparisonI = int(matrixR[C-1,C-2] * (10**(accuracy)) + 0.5)
        comparisonC = int((matrixR[C-1,C-2] + matrixE[C-1,C-1]) * (10**(accuracy)) + 0.5)
    
    if (comparisonI != comparisonC):
        N = N * 2
        C = C + 1
        matrixDummy = np.zeros((1,C))
        matrixR = np.vstack((matrixR,matrixDummy))
        matrixE = np.vstack((matrixE,matrixDummy))

        matrixDummy = np.zeros((C+1,1))
        matrixR = np.hstack((matrixR,matrixDummy))
        matrixE = np.hstack((matrixE,matrixDummy))

    
#Making the matrix prettier by cropping the unnecessary row and column.
matrixR = np.delete(matrixR,(C),axis=0)
matrixR = np.delete(matrixR,(C),axis=1)
matrixE = np.delete(matrixE,(C),axis=0)
matrixE = np.delete(matrixE,(C),axis=1)

#printing outputs
print "Target accuracy reached at N =", N, "slices."
print 'Rombergs Technique second last term: ', matrixR[C-1,C-2]
print 'Rombergs Technique last term: ', matrixR[C-1,C-1]
print 'Estimated error range: ', matrixE[C-1,C-1]

#Fancy triangular tables
y_n = "N"

print ' '
y_n = raw_input("Would you like to see the results in a triangular table? Y or N: ")
while ((y_n != "Y") and (y_n != "N")):
    print "Please make sure to enter only 'Y' or 'N' without the quotes!"
    y_n = raw_input("Would you like to see the results in a triangular table? Y or N: ")

print' '
if (y_n == 'Y'):
    print "Romberg's Results: "
    print matrixR
print ' '

y_n = "N"

print ' '
y_n = raw_input("Would you like to see the estimated errors in a triangular table? Y or N: ")
while ((y_n != "Y") and (y_n != "N")):
    print "Please make sure to enter only 'Y' or 'N' without the quotes!"
    y_n = raw_input("Would you like to see the estimated errors in a triangular table? Y or N: ")

#Romberg's Integration Technique by scipy
print' '
if (y_n == 'Y'):
    print "Corresponding Error Estimate: "
    print matrixE

#Varifying results with scipy's Romberg's integration techniques.
y_n = "N"

print ' '
y_n = raw_input("Would you like to check it with scipy's Romberg result? Y or N: ")
while ((y_n != "Y") and (y_n != "N")):
    print "Please make sure to enter only 'Y' or 'N' without the quotes!"
    y_n = raw_input("Would you like to check it with scipy's Romberg result? Y or N: ")

#Romberg's Integration Technique by scipy
print' '
if (y_n == 'Y'):
    result = integrate.romberg(f, a, b, tol=(1.48e-08), rtol=(1.48e-08), show = True)
    print ' '
    print "Author's Note: "
    print "The scipy Romberg's output accuracy was based on absolute/relative "
    print "tolerance of 1.48e-08%, hence the different evalutions. Though the "
    print "calculated values remains similar, if not the same."
    print "Try input the 11th decimal place accuracy for the exact evaluation."
#################
# Comment:
# I've been playing around with the scipy's tol (absolute tolerance) and 
#   rtol (relative tolerance). What I've realized is that these two relies on
#   the % of the last and second last terms, whereas on the lab assignments it
#   was stated to find accracy for the error to reach the 6th decimal instead.
#   Hence different results for different definition of accuracy.
#
# I have set the scipy's tol and rtol as the original default %, though the 
#   boundries will still scale with the initial input for easier comparison.
##################