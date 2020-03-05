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
# paramter: numpy array of accelerations, length of pendulum
# return:   numpy array of angular positions
def calcTheta(accelerations, length):
    accs = accelerations.astype(np.float)
    thetas = np.arctan(np.divide(accs,length))
    
    return thetas
    
    
# function: graphTheta
# purpose:  takes an array of angular positions and an array of times 
#           and graphs the variables (angular position vs time)
# paramter: numpy array of thetas (radians) of accelerations and numpy of 
#           time (seconds)
# return:   void
def graphTheta(theta, time):
    x = time.astype(np.float)   #from array of strings to floats
    y = theta.astype(np.float)  #from array of strings to floats
    plt.plot(x, y, "-bo")
    plt.ylabel("Angular Position (radians)")
    plt.xlabel("Time (s)")
    plt.title("Pendulum Acceleration vs Time")
    plt.show()
    
# function: calcPeriod
# purpose:  finds the period of the pendulum
# paramter: TODO
# return:   TODO
def calcPeriod(acc, time):
    acc  = acc.astype(np.float)   #from array of strings to floats
    time = time.astype(np.float)  #from array of strings to floats
    periods = np.empty(0, dtype=float)
    
    for i in range(1,len(acc)):
        if (acc[i-1] > 0 and acc[i] < 0):
            periods = np.append(periods, (time[i-1] + time[i])/2)
            
    avg_period = 0
    for elem in periods:
        avg_period = avg_period + elem
        
    return avg_period / len(periods)

# MAIN SCRIPT
###################################

acc_x21 = getAcc('Data21.csv')
time21  = getTime('Data21.csv')
#graphAcc(acc_x21,time21)

acc_x17 = getAcc('Data17.csv')
time17  = getTime('Data17.csv')
#graphAcc(acc_x17,time17)

acc_x13 = getAcc('Data13.csv')
time13  = getTime('Data13.csv')
#graphAcc(acc_x13,time13)

acc_x9 = getAcc('Data9.csv')
time9  = getTime('Data9.csv')
#graphAcc(acc_x9,time9)

acc_x5 = getAcc('Data475.csv')
time5  = getTime('Data475.csv')
#graphAcc(acc_x5,time5)
thetas21 = calcTheta(acc_x21, 21.0)
graphTheta(thetas21,time21)
period = calcPeriod(acc_x21,time21)
print(period)