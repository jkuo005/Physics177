# -*- coding: utf-8 -*-
"""
Physics 177
Final Project
Orbit Integrator for a particle within an NFW halo using the Leap Frog method
@author: Jeff Kuo
SID: 860884131
"""
#######################
# Initialization
#######################
import numpy as np
import matplotlib.pyplot as plt
import pdb
#######################
# Parameters
#######################
#G  = 6.67384e-11   #gravitational constant in Newton *
                                            # meters^2 /
                                            # kg^2
#G = 4.5e2
G = 4.3e-6
                   #gravitational constant in kiloparsec^3 /
                                            #mass of sun
                                            #gigayear^2

vo = 178.0          #Virial Overdensity
rv = 258.0          #Virial radius in KiloParsecs
rs = 21.5           #Scale Radius
#pc0= 9.47 * 10**-27 #present critical density in kg/m^3
#pc0= 1.393e-8
pc0= 1.393e2

                      #present critical density in mass of sun /
                                                #kiloparsec^3

c  = rv / rs        #the concentration parameter
                    #c = 12
#M_v  = 1.0e12       #Mass of the Halo (From Fortran program)

g_c = 1./( np.log(1. + c) - (c/(1.+c)) )
                    #Refers to g(c)

d_char = (vo * c**3 * g_c) / 3.
                    #characteristic density

M_v = (4./3.)*np.pi*(rv**3)*vo*pc0
                    #mass of the halo
                    #M_v = 1.783e12
#M_v = 1.e12
#M_v = 3.e12

#######################
# Functions
#######################

#####
# Note:
# s = r / rv
# where r is the actual radius
#####
def NFWacc(rx,ry,rz):
    r = np.sqrt(rx**2 + ry**2 + rz**2)
    c = 12.
    #G = 4.5e-6    #gravitational constant
    #G = 4.5e2 
    G = 4.3e-6
    vo = 178.0          #Virial Overdensity
    rv = 258.0          #Virial radius in KiloParsecs
    rs = rv/c           #Scale Radius
    #pc0= 1.393e-8 #present critical density
    pc0= 1.393e2
    g_c = 1./( np.log(1. + c) - (c/(1.+c)) )

    s = r / rv
    #s=1  #Kepler's problem: mass is constant instead of radius dependent

    M_v = (4./3.)*np.pi*(rv**3)*vo*pc0
    
    M = M_v * g_c * ( np.log(1. + c*s) - c*s / (1. + c*s) )
    #pdb.set_trace()
    ax = -G*M*rx/r**3
    ay = -G*M*ry/r**3
    az = -G*M*rz/r**3
    
    return [ax,ay,az] 

#N=1000
#t = np.linspace(0,1,1000,dtype=float)

#######################
# Initial Conditions
# ---User Inputs----
#######################
pos = np.zeros(3)
vel = np.zeros(3)

print "Input the following: "
print "1 for custom set of coordinates and initial velocities"
print "2 for a preset of coordinates"
userInput = int(input("Enter the option: "))
while userInput != 1 and userInput != 2:
    userInput = int(input("Please make sure it is 1 or 2: "))

#prompt for initial conditions
if userInput == 1:
    print "Initial Position (Kiloparsecs)"
    pos[0] = float(input("x0 = "))
    pos[1] = float(input("y0 = "))
    pos[2] = float(input("z0 = "))
    #range from 10 to 100
    
    print "Initial Velocity (km/s)"
    vel[0] = float(input("v0x = "))
    vel[1] = float(input("v0y = "))
    vel[2] = float(input("v0z = "))
    #range from 0 to 20
    
    t = int(input("Elapsed gigayears (in integers): "))
    
    # range from 5 to 100

#preset of coordinates and initial velocities

elif userInput == 2:
    pos[0] = float(-0.8)
    pos[1] = float(-41.5)
    pos[2] = float(-29.9)
    
    vel[0] = float(-86.)
    vel[1] = float(-268.)
    vel[2] = float(256.)
    
    t = 14
    #t = 14  #Age of universe
####
# Interesting Presets
# The four leaf clover
# pos(100,100,200), vel(-50,50,100), t=50

#######################
# Leap Frog
#######################
x = []
xhalf = 0
y = []
yhalf = 0
z = []
zhalf = 0

xvel = []
xvelhalf = 0
yvel = []
yvelhalf = 0
zvel = []
zvelhalf = 0

x.append(pos[0])
y.append(pos[1])
z.append(pos[2])
xvel.append(vel[0])
yvel.append(vel[1])
zvel.append(vel[2])

dt=0.01
#dt = -0.01         #Reversed Leap Frog

time = [0]

#Initial Euler's
xhalf = x[0] + 0.5*dt*xvel[0]
yhalf = y[0] + 0.5*dt*yvel[0]
zhalf = z[0] + 0.5*dt*zvel[0]

xvelhalf = xvel[0] + 0.5*dt*NFWacc(x[0],y[0],z[0])[0]
yvelhalf = yvel[0] + 0.5*dt*NFWacc(x[0],y[0],z[0])[1]
zvelhalf = zvel[0] + 0.5*dt*NFWacc(x[0],y[0],z[0])[2]

#Conservation of Energy, initial condition
r0 = np.sqrt(x[0]**2 + y[0]**2 + z[0]**2)
                                    #Initial Radius
s0 = r0/rv
M0 = M_v * g_c * ( np.log(1. + c*s0) - c*s0 / (1. + c*s0) )
                                        #Initial Mass
V0 = np.sqrt(xvel[0]**2 + yvel[0]**2 + zvel[0]**2)
                                    #Modulus velocity

energy = [] #total energy level
            #E = K + T
K = []      #potential energy at given point
            #K = GM/r
T = []      #kinetic energy at given point
            #T = 1/2 * V^2

K0 = -G * M0 / r0
        #Initial Potential Energy
T0 = 0.5 * V0**2
        #Initial Kinetic Energy
K.append(K0)
T.append(T0)
energy.append(K[0] + T[0])

#Velocity
Vr = [] #Radial Velocity
        #Vr = (x*vx + y*vy + z*vz) / r

Vr.append(( x[0]*xvel[0] + y[0]*yvel[0] + z[0]*zvel[0] ) / r0)
        #Initial Radial Velocity

Vt = [] #Tangential Velocity
        #sqrt( V**2 - Vr**2)

Vt.append(np.sqrt( V0**2 - Vr[0]**2 ))

#Leap Frog
Mstore=[M0]
for i in range(t*100):
    xvel.append(xvel[-1]+NFWacc(xhalf, yhalf, zhalf)[0]*dt)
    x.append(x[-1] + dt*xvelhalf)

    yvel.append(yvel[-1]+NFWacc(xhalf, yhalf, zhalf)[1]*dt)
    y.append(y[-1] + dt*yvelhalf)

    zvel.append(zvel[-1]+NFWacc(xhalf, yhalf, zhalf)[2]*dt)
    z.append(z[-1] + dt*zvelhalf)
    
    xhalf += dt * xvel[-1]    
    yhalf += dt * yvel[-1]    
    zhalf += dt * zvel[-1]    
    
    xvelhalf += dt * NFWacc(x[-1],y[-1],z[-1])[0]
    yvelhalf += dt * NFWacc(x[-1],y[-1],z[-1])[1]
    zvelhalf += dt * NFWacc(x[-1],y[-1],z[-1])[2]
    
    #Energy
    rad = np.sqrt(x[-1]**2 + y[-1]**2 + z[-1]**2) #radius
    s = rad/rv
    Mass = M_v * g_c * ( np.log(1. + c*s) - c*s / (1. + c*s) ) #modulus mass
    Mstore.append(Mass)
    V = np.sqrt(xvel[-1]**2 + yvel[-1]**2 + zvel[-1]**2) #modulus velocity
    
    K.append(-G*Mass / rad)
    T.append(0.5 * V**2)
    energy.append(K[-1] + T[-1])
    
    #Velocity
    Vr.append(( x[-1]*xvel[-1] + y[-1]*yvel[-1] + z[-1]*zvel[-1] ) / rad)
                #Radial Velocity
    
    Vt.append(np.sqrt( V**2 - Vr[-1]**2))
                #Tangential Velocity
    
    time.append((i+1)*dt)
#pdb.set_trace()
radius = (np.array(x)**2+np.array(y)**2+np.array(z)**2)**0.5

energy_rat = np.array(energy) / energy[0]
#######################
# Plotting
#######################
#Radius WRT Time
plt.figure(1)
plt.plot(np.array(time),radius, 'k')
plt.xlabel('time [Gyr]',fontsize=20)
plt.ylabel('r [kpc]', fontsize=20)
plt.savefig('radius WRT t.png', format = 'png')

#Energy Ratio WRT Time
plt.figure(2)
plt.plot(np.array(time),energy_rat)
plt.plot(np.array(time),T[:]/energy[0], 'r')
plt.plot(np.array(time),K[:]/energy[0],'g')

plt.xlabel('time [Gyr]',fontsize=20)
plt.ylabel('Energy ratio',fontsize=20)

plt.savefig('energy WRT t.png', format = 'png')

#Radial Velocity
plt.figure(3)
plt.plot(np.array(time),Vr)
plt.xlabel('time [Gyr]',fontsize=20)
plt.ylabel('Rad. Velocity',fontsize=20)

plt.savefig('rad vel WRT t.png', format = 'png')


#Tangential Velocity
plt.figure(4)
plt.plot(np.array(time),Vt)
plt.xlabel('time [Gyr]',fontsize=20)
plt.ylabel('Tan. Velocity',fontsize=20)

plt.savefig('tan vel WRT t.png', format = 'png')

"""
#Test Angular momentum
plt.figure(5)
plt.plot(radius,Vt)
plt.xlabel('r [kpc]',fontsize=20)
plt.ylabel('Tan. Velocity',fontsize=20)
"""
"""
# test energy
plt.figure(6)
plt.plot(radius,energy_rat)
plt.plot(radius,T[:]/energy[0], 'r')
plt.plot(radius,K[:]/energy[0],'g')

plt.xlabel('radius [kpc]',fontsize=20)
plt.ylabel('Energy ratio',fontsize=20)
"""

#Projectile Path
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)
plt.savefig('3D path.png', format = 'png')
