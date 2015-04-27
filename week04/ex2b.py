# -*- coding: utf-8 -*-
"""
Physics 177
Lab Assignment 3, exercise 2b
Gaussian Elimination
@author: Jeff Kuo
SID: 860884131
"""

import numpy as np
from numpy.linalg import solve

#Definition of the arrays
Vplus = 5.

A = np.array([[4,-1,-1,-1],[-1,3,0,-1],[-1,0,3,-1],[-1,-1,-1,4]],float)
v = np.array([Vplus,0,Vplus,0],float)

N = len(v)

#Gaussian Process
for m in range(N):
    pivot = A[m,m]
    A[m,:] /= pivot
    v[m] /= pivot

    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult * A[m,:]
        v[i] -= v[m] * mult

#Backsubstitution
Vnum = np.array([0.,0.,0.,0.],float)
for m in range(N-1,-1,-1):
	Vnum[m] = v[m]
	for i in range(m+1,N):
		Vnum[m] -= A[m,i] * Vnum[i]

#Results
for c in range(N):
    print "V%s = " %(c+1), Vnum[c], 'volts'