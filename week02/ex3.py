# -*- coding: utf-8 -*-
"""
Physics 177
Lab Assignment 2, exercise 3
Integration with Trapezoidal/Simpson's rule
@author: Jeff Kuo
SID: 860884131
"""
#Initialization
import numpy as np
from scipy.integrate import trapz, simps

#Functions - a subroutine
def f(x):
    return  x**4 - 2.*x + 1.

#Definition of Variables and Arrays
N = 20          #Make sure N is even, otherwise inaccurate results for simpsons
a = 0.0                      #boundry A
b = 2.0                      #boundry B
switch = 0      #Dummy Integer

"""
------------------------------- #Trapezoidal -------------------------------
"""
TI1 = 0.5*f(a) + 0.5*f(b)
TI2 = 0.5*f(a) + 0.5*f(b)

#N=10
while (switch < 1):
    N = 10
    h = (b-a) / float(N)
    for k in range(1,N):
        TI1 += f(a + k*h)

    TI1 = TI1 * h
    switch += 1
#N=20
N = 20
h = (b-a) / float(N)
for k in range(1,N):
    TI2 += f(a + k*h)

TI2 = TI2 * h

print 'Trapezoidal Integration (N=10) result =', TI1
print 'Trapezoidal Integration (N=20) result =', TI2
print ' '

"""
-------------------------------- #Simpson's ---------------------------------
"""
SI1 = f(a) + f(b)
SI2 = f(a) + f(b)
#N=10
switch = 0
while (switch < 1):
    N = 10
    h = (b-a) / float(N)
    for k in range(1, (N/2) + 1): #Repeating Even
        SI1 += (4.0 * f( a + (2. * float(k) - 1.) * h ))
    
    for k in range(1, (N/2)): #Repeating Odd
        SI1 += (2.0 * f( a + (2. * float(k)) * h ))

    SI1 = SI1 * ((1.0 / 3.0) * h)
    switch += 1

#N=20
N = 20
h = (b-a) / float(N)

for k in range(1, (N/2) + 1): #Repeating Even
    SI2 += (4.0 * f( a + (2. * float(k) - 1.) * h ))
    
for k in range(1, (N/2)): #Repeating Odd
    SI2 += (2.0 * f( a + (2. * float(k)) * h ))

SI2 = SI2 * ((1.0 / 3.0) * h)
print 'Simpsons Integration (N=10) result =', SI1
print 'Simpsons Integration (N=20) result =', SI2

"""
--------------------------- #scipy integration -----------------------------
"""

counter = 0     #Dummy integer counter
array_F = np.zeros(N+1)
while (counter < (N+1)):
    array_F[counter] = f( a + (float(counter) * h) )
    counter = counter + 1
print ' '
#scipy trapezoidal        
STI = trapz(array_F, dx=h)
print 'Scipy Trapezoidal Integration result =', STI

#scipy simpson's
SSI = simps(array_F, dx=h)
print 'Scipy Simpsons Integration result =', SSI

print ' '

"""
---------------------------- Error Estimation ------------------------------
"""
#Trapezoidal Error
eT = (1./3.) * (TI2 - TI1)
print 'Trapezoidal Error Estimation =', eT
TI = TI2 + eT
print 'Theoretically Correct Trapezoidal Result =', TI
print ' '

eS = (1./15.) * (SI2 - SI1)
print 'Simpsons Error Estimation =', eS
SI = SI2 + eS
print 'Theoretically Correct Simpsons Result =', SI
print ' '


#Actual Calculation
""" For future use
res = input('Expected Integration Value: ')
"""
res = 4.4
print 'Actual integration by hand result =', res #4.4 for current problem
print ' '
print 'Comparing theoretical results with actual result...'
percTI = abs(((res - TI) / res) * 100.)
print 'Percent Difference for Trapezoidal Result =', percTI, '%'
percSI = abs(((res - SI) / res) * 100.)
print 'Percent Difference for Simpsons Result =', percSI, '%'