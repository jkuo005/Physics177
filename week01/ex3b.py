# -*- coding: utf-8 -*-
"""
@author: Jeff Kuo 860884131
"""
import numpy as np
import matplotlib.pyplot as plt
import math
import pdb


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

array_T = np.zeros(11) #Array for time
array_V = np.zeros(11) #Array for velocity

range_T = 0.0       #dummy variable for plotting later

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

if (v_seg < 0):
    print "Computational Error!!!"
    print "Please make sure Max Velocity > Min Velocity!"

else:
    while (int_counter <= 10):
        print int_counter
        
        #Initial velocity    
        v_init = ( v_min + ( float(int_counter) * v_seg ))
        print "When initial velocity is", v_init, "m/s"
        array_V[int_counter] = v_init
    
        #Quadratic Formula
        var_Root = np.sqrt( pow(v_init,2) + ( 2. * cons_G * cons_H ) )
    
        #Time elapsed
        var_T = (( 1. / cons_G ) * ( -(v_init) + var_Root ))
        print "It takes ", var_T, "seconds for the object to reach the ground."
        
        #Array for Time and Velocity
        array_T[int_counter] = var_T
        
        if (int_counter < 1):
            range_T = var_T
    
        #Integer Counter
        int_counter = int_counter + 1
        print " "
    
        #Plotting
        plt.plot(v_init, var_T, 'bo')
        plt.gray()

    #Saving txt file for ASCII
    array_Matrix = np.vstack((array_T,array_V)).T
    
    np.savetxt('Time vs Velocity Results.txt',array_Matrix,fmt='%10.4f')
    
    #Plotting Line
    plt.plot(array_V, array_T, 'b-')

    #Naming Title and Axis
    plt.title("T(V)")
    plt.xlabel("Initial Velocity [m/s]")
    plt.ylabel("Time [s]")
    plt.show

    #Adjusting range
    plt.ylim([0,range_T])

    #Printing Image
    plt.savefig('Time as a function of Velocity.png', format = 'png')
    
    
    
    """
    a = np.ones(10)
    np.savetxt('testfile.txt',a,fmt='%5.3f')
    np.savetxt('testfile.txt',a,fmt='%18.3e')
    """