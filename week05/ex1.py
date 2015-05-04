# -*- coding: utf-8 -*-
"""
Physics 177
Lab Assignment 5, exercise 1
Finding the roots of a polynomial
@author: Jeff Kuo
SID: 860884131
"""

import numpy as np
import scipy.optimize as opt
import matplotlib.pylab as plt
import math

#####################
# Function
#####################
def P(x):
    return 924.*(x**6) - 2772.*(x**5) + 3150.*(x**4) - 1680.*(x**3) + 420.*(x**2) - 42*x + 1
    
#####################
# Plotting
#####################
x = np.linspace(0,1,num=200,dtype=float)
y = P(x)

ax = plt.subplot(111)
plt.plot(x,y,'r',linewidth=3)

#axis line for the graph
t = np.zeros(x.size)
plt.plot(x,t,'black',linewidth=1)

#save file
plt.savefig('Polynomial Plot.png', format = 'png')

"""
Side Note
Roots roughly at: 
x0 = 0.034
x1 = 0.169
x2 = 0.381
x3 = 0.618
x4 = 0.830
x5 = 0.966
"""
roots = np.array((0.034,0.169,0.381,0.618,0.830,0.966))
solve = np.zeros(roots.size)

#####################
# Finding Roots
#####################
for i in range(roots.size):
    solve[i] = opt.newton(P, roots[i], tol=1.e-10, maxiter=50)
    print "x%s =" %(i+1), solve[i]