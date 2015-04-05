"""
Lab Assignment 1
ex2. Students' Final Grades
Jeff Kuo - 860884131
"""

#Initialization
import numpy as np
import matplotlib.pyplot as plt
import math


#Defining Vectors/Arrays and Variables
H = np.array([10.0,10.0,8.0,9.5,3.0,9.0,0.0,6.0])   #Homework
M = np.array([10.0,10.0,10.0,10.0,8.0,5.0,10.0,7.0])#Mid-Term
F = np.array([9.0,10.0,10.0,6.0,10.0,6.0,8.0,9.0])  #Final Project
T = np.array([0.,0.,0.,0.,0.,0.,0.,0.])             #Total Grades

fail_Students = 0	      #Students who failed
good_Students = 0      #Outstanding students
int_Counter   = 0      #A counter for conditional loops


#fluff, for my own amusement
print "Saved grades: "
print "Homework:      "
print H
print "Mid-term:      "
print M
print "Final Project: "
print F


#Calculation
print " "
print "Calculation in progress..."
T = ( ( H * 0.4 ) + ( M * 0.2 ) + ( F * .4) )	#All the grades 


#Print to Screen
print "Final Grades:  "
print T
print " "
while (int_Counter < 8):						#Column of grades
	print "Student ", int_Counter + 1, ": ", T[int_Counter]
	int_Counter = int_Counter + 1
print " "
	
#Filtering failed Students
int_Counter = 0
#Need to reset the counter, otherwise it starts at 8 from previous loop
while (int_Counter < 8):
	if (T[int_Counter] < 6.0):
		fail_Students = fail_Students + 1
	int_Counter = int_Counter + 1
	
print "The number of failed students: ", fail_Students


#Filtering outstanding Students
int_Counter = 0
while (int_Counter < 8):
	if (T[int_Counter] > 9.5):
		good_Students = good_Students + 1
	int_Counter = int_Counter + 1

print "The number of outstanding students: ", good_Students
print " "

#Histogram of the grades
print "Generating histogram..."
plt.hist(T)
plt.title("Student Grades")
plt.xlabel("Final Grade")
plt.ylabel("Number of Students")

print "Printing histogram..."
plt.show
plt.savefig('StudentGrades.png', format = 'png')