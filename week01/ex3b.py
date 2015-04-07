# -*- coding: utf-8 -*-
"""
@author: Jeff Kuo 860884131
"""
import numpy as np
import matplotlib.pyplot as plt
import math

#initialization
cons_G = 9.81       #Gravity
v_init = 0.0        #Initial velocity
v_min  = 0.0        #minimum velocity
v_max  = 0.0        #maximum velocity
v_seg  = 0.0        #velocity segment
var_T  = 0.0        #elapsed time
cons_H = 800.0      #Height
var_Root = 0.0      #For calculation
int_counter = 0     #Dummy Integer

range_T = 0.0       #dummy variable for plotting later



#plot
t_v = plt.plot(111)

#User input
print "Positive direction for velocity is the same as gravity (downwards). "
v_min = input("Enter minimum velocity [meters per second]: ")
v_max = input("Enter maximum velocity [meters per second]: ")

#Calculation
print "Calculating outcome..."

#loop for calculating t from min
v_seg  = (( v_max - v_min ) / 10.)
print "Velocity segment is ", v_seg, "m/s"
print " "

while (int_counter <= 10):
    #Initial velocity    
    v_init = ( v_min + ( float(int_counter) * v_seg ))
    print "When initial velocity is", v_init, "m/s"
    
    #Quadratic Formula
    var_Root = np.sqrt( pow(v_init,2) + ( 2. * cons_G * cons_H ) )
    
    #Time elapsed
    var_T = (( 1. / cons_G ) * ( -(v_init) + var_Root ))
    print "It takes ", t, "seconds for the object to reach the ground."
    
    if (int_counter < 1):
        range_T = var_T
    
    #Integer Counter
    int_counter = int_counter + 1
    print " "
    
    #Plotting
    plt.plot(v_init, var_T, 'bo')
    plt.gray()

#Naming Title and Axis
plt.title("Time vs Velocity")
plt.xlabel("Initial Velocity [m/s]")
plt.ylabel("Time [s]")
plt.show

#Adjusting range
plt.ylim([0,range_T])