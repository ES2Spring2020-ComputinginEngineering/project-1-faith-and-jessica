# Project 1
# Step 4
# Analysis of Results
#
# Jessica Nordlund 
# Faith Seely
# 
##################################

# IMPORT STATEMENTS
##################################
import matplotlib.pyplot as plt
import numpy as np
import os
import csv



# CUSTOM FUNCTION DEFINITIONS
###################################

# function: getAcc
# purpose:  gets the x acceleration from the given file and returns it as an
#           array
# paramter: filename (where data is located)
# return:   array of x accelerations
def getAcc(filename): 
    acc_x    = np.empty(0, dtype=float)
    raw_data = open(filename)
    data_csv = csv.reader(raw_data)
    
    for row in data_csv:
        if (len(row) != 0):
            acc_x = np.append(acc_x, row[0])  
    
    return acc_x
        

# function: getTime
# purpose:  gets the time stamps from the given file and returns them as an
#           array
# paramter: filename (where data is located)
# return:   array of times
def getTime(filename): 
    times    = np.empty(0, dtype=float)
    raw_data = open(filename)
    data_csv = csv.reader(raw_data)
    
    for row in data_csv:
        if (len(row) != 0):
            times = np.append(times, row[3])  
    
    return times
        

# function: graphAcc
# purpose:  takes an array of accelerations and an array of time of a pendulum 
#           and graphs the variables (accelerations vs time)
# paramter: numpy array of accelerations (milli-g) of pendulum and numpy of 
#           time (seconds)
# return:   void
def graphAcc(accs,time):
    x = time.astype(np.float)   #from array of strings to floats
    y = accs.astype(np.float)   #from array of strings to floats
    plt.plot(x, y, "-bo")
    plt.ylabel("Acceleration (milli-g)")
    plt.xlabel("Time (s)")
    plt.title("Pendulum Acceleration vs Time")
    plt.show()
    
# function: calcTheta
# purpose:  finds the theta values from a given set of accelerations
# paramter: numpy array of accelerations
# return:   numpy array of angular positions
def calcTheta(accelerations):
    # THETA CALC
    return 0
    
# function: graphTheta
# purpose:  takes an array of angular positions and an array of times 
#           and graphs the variables (angular position vs time)
# paramter: numpy array of thetas (radians) of accelerations and numpy of 
#           time (seconds)
# return:   void
def graphTheta(theta, time):
    plt.plot(time, theta, "-bo")
    plt.ylabel("Angular Position (radians)")
    plt.xlabel("Time (s)")
    plt.title("Pendulum Acceleration vs Time")
    plt.show()
    
# function: calcPeriod
# purpose:  finds the period of the pendulum
# paramter: TODO
# return:   TODO
def calcPeriod():
    # PERIOD CALC
    return 0

# MAIN SCRIPT
###################################

acc_x = getAcc('Pendulum21.csv')
time  = getTime('Pendulum21.csv')
print(acc_x)
print(time)
graphAcc(acc_x,time)
#thetas = calcTheta(acc_x)
#graphTheta(thetas,times)