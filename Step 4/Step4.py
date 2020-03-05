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
import pandas



# CUSTOM FUNCTION DEFINITIONS
###################################

# function: getData
# purpose:  gets the raw data from a file and puts the data in corresponding
#           global variable
# paramter: filename to get data from
# return:   void
def getData(filename, accelerations, times): 
    emptyArray = np.empty(0, dtype=float)
    #raw_data = pandas.read_csv(filename)
    raw_data = open(filename)
    data_csv = csv.reader(raw_data)
    
    for row in data_csv:
        if (row != emptyArray):
            accelerations = np.append(accelerations, {row[0]})  
            times         = np.append(times, {row[3]})  
        print (row)
        
    print(accelerations)
    print(times)

        

# function: graphAcc
# purpose:  takes an array of accelerations and an array of time of a pendulum 
#           and graphs the variables (accelerations vs time)
# paramter: numpy array of accelerations (milli-g) of pendulum and numpy of 
#           time (seconds)
# return:   void
#
# Due to the way our microbit is oriented, the acceleration is the 
# acceleration along the x-axis.
def graphAcc(accs,time):
    plt.plot(time, accs, "-bo")
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
acc_x = np.empty(0, dtype=float)
time  = np.empty(0, dtype=float)
getData('Pendulum21.csv', acc_x, time)
print(acc_x)
print(time)
#graphAcc(acc_x,times)
#thetas = calcTheta(acc_x)
#graphTheta(thetas,times)