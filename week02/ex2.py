# -*- coding: utf-8 -*-
"""
Physics 177
Lab Assignment 2, exercise 2
Integration with Trapezoidal/Simpson's rule
@author: Jeff Kuo
SID: 860884131
"""

#Initialization
import numpy as np
import matplotlib.pyplot as plt

#Importing Data from .txt file
print 'Importing file...'
data = np.genfromtxt('velocities.txt')

print 'Compiling datas...'
#time array
time = data[:,][:,0]

#velocity array
velocity = abs(data[:,][:,1])
vel_graph = data[:,][:,1]

#distance/displacement array
distance = np.zeros(101)
displacement = np.zeros(101)
disp_Simp = np.zeros(51)
spec_Time = np.zeros(51)

#Defining Variables, Integers, and dummy objects
N = np.size(time) - 1
a = float(time[0])
b = float(time[N])
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
    base = ( vel_graph[counter] + vel_graph[counter + 1] )
    area = ( base * height ) / 2.
    TIX += area
    displacement[counter+1] = TIX
    counter += 1

print 'Approximate Particle Displacement (Trapezoidal): ', TIX,'m'

#Simpson's Rule
"""
SIX = vel_graph[0] + vel_graph[N]
for k in range(1, (N/2) + 1): #Repeating Even
    SIX += (4.0 * vel_graph[2*k - 1])
    
for k in range(1, (N/2)): #Repeating Odd
    SIX += (2.0 * vel_graph[2*k])
SIX = SIX * ((1.0 / 3.0) * height)
"""


counter = 0
while (counter < N):
    area=(vel_graph[counter]+4.*vel_graph[counter+1]+vel_graph[counter+2])
    area*=((1./3.)*height)
    SIX += area
    disp_Simp[counter/2 + 1] = SIX
    counter += 2
    spec_Time[counter/2] = float(counter)

print 'Approximate Particle Displacement (Simpsons): ', SIX,'m'
print ' '

"""
                    Approximating Total Distance
"""
#Trapezoidal Rule
counter = 0
while (counter < N):
    base = ( velocity[counter] + velocity[counter + 1] )
    area = ( base * height ) / 2.
    TI += area
    distance[counter+1] = TI
    counter += 1

print 'Approximate Total Distance Traveled (Trapezoidal): ', TI,'m'

#Simpson's Rule
SI = velocity[0] + velocity[N]
for k in range(1, (N/2) + 1): #Repeating Even
    SI += (4.0 * velocity[2*k - 1])
    
for k in range(1, (N/2)): #Repeating Odd
    SI += (2.0 * velocity[2*k])

SI = SI * ((1.0 / 3.0) * height)
print 'Approximate Total Distance Traveled (Simpsons): ', SI,'m'
print ' '


#Saving txt file
print 'Saving results as Distance vs Time [Method].txt'
trap_Matrix = np.vstack((time,displacement)).T
simp_Matrix = np.vstack((spec_Time,disp_Simp)).T

np.savetxt('Distance vs Time Trapezoidal.txt',trap_Matrix,fmt='%10.6f')
np.savetxt('Distance vs Time Simpsons.txt',simp_Matrix,fmt='%10.6f')


#Plotting
print 'Plotting and graphing...'

plt.subplot(3,1,1)
plt.plot(spec_Time, disp_Simp, 'r-')
plt.title("Displacement as f(t)")
plt.ylabel("Displacement [m]")

plt.subplot(3,1,2)
plt.plot(time, vel_graph, 'b-')
plt.title("Velocity as f(t)")
plt.ylabel("Velocity [m/s]")

plt.subplot(3,1,3)
plt.plot(time, distance, 'r-')
plt.title("Distance as a f(t)")
plt.ylabel("Distance [m]")
plt.xlabel("Time [s]")

plt.show
plt.savefig('Distance.png', format = 'png')