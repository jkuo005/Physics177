# -*- coding: utf-8 -*-
"""
Physics 177
Lab Assignment 3, exercise 2b
LU Decomposition
@author: Jeff Kuo
SID: 860884131
"""

import numpy as np
import scipy as sp
from numpy.linalg import solve
from scipy.linalg import lu

#Definition of the arrays
Vplus = 5.

A = np.array([[4,-1,-1,-1],[-1,3,0,-1],[-1,0,3,-1],[-1,-1,-1,4]],float)
v = np.array([Vplus,0,Vplus,0],float)

N = len(v)
#LU decomposition from scipy
P,L,U = lu(A)
"""
print P

print L

print U
"""
#Solving the system with LU decomposition
#LY = B
y = solve(L,v)

"""
print y
"""
#UX = Y
x = solve(U,y)

"""
print x
"""
#Results
for c in range(N):
    print "V%s = " %(c+1), x[c], 'volts'