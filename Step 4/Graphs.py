# Project 1
# Step 4
# Analysis of Results
# Graphs.py
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
import scipy.signal



# CUSTOM FUNCTION DEFINITIONS
###################################

# function: getAccX
# purpose:  gets the x acceleration from the given file and returns it as an
#           array
# paramter: filename (where data is located)
# return:   array of x accelerations (floats)
def getAccX(filename): 
    acc_x    = np.empty(0, dtype=float)
    raw_data = open(filename)
    data_csv = csv.reader(raw_data)
    
    for row in data_csv:
        if (len(row) != 0):
            acc_x = np.append(acc_x, row[0])  
    
    acc_x = acc_x.astype(np.float)     #from array of strings to floats
    return scipy.signal.medfilt(acc_x)

# function: getAccY
# purpose:  gets the y acceleration from the given file and returns it as an
#           array
# paramter: filename (where data is located)
# return:   array of y accelerations (floats)
def getAccY(filename): 
    acc_y    = np.empty(0, dtype=float)
    raw_data = open(filename)
    data_csv = csv.reader(raw_data)
    
    for row in data_csv:
        if (len(row) != 0):
            acc_y = np.append(acc_y, row[1])  
    
    acc_y = acc_y.astype(np.float)     #from array of strings to floats
    return scipy.signal.medfilt(acc_y)

# function: getAccZ
# purpose:  gets the z acceleration from the given file and returns it as an
#           array
# paramter: filename (where data is located)
# return:   array of z accelerations (floats)
def getAccZ(filename): 
    acc_z    = np.empty(0, dtype=float)
    raw_data = open(filename)
    data_csv = csv.reader(raw_data)
    
    for row in data_csv:
        if (len(row) != 0):
            acc_z = np.append(acc_z, row[2])  
    
    acc_z = acc_z.astype(np.float)     #from array of strings to floats
    return scipy.signal.medfilt(acc_z)
        

# function: getTime
# purpose:  gets the time stamps from the given file and returns them as an
#           array
# paramter: filename (where data is located)
# return:   array of times (floats)
def getTime(filename): 
    times    = np.empty(0, dtype=float)
    raw_data = open(filename)
    data_csv = csv.reader(raw_data)
    
    for row in data_csv:
        if (len(row) != 0):
            times = np.append(times, row[3])  
    
    times = times.astype(np.float)     #from array of strings to floats
    return times
        

# function: graphAcc
# purpose:  takes 3 arrays of accelerations and an array of time of a pendulum 
#           and graphs the variables (accelerations vs time)
# paramter: numpy arrays of accelerations (milli-g) of pendulum and numpy of 
#           time (seconds)
# return:   void
def graphAcc(acc_x, acc_y, acc_z,time):    
    plt.subplot(311)
    plt.plot(time, acc_x, "b")
    plt.xlabel("Time (s)")
    plt.title("Pendulum Acceleration vs Time")
    plt.legend('X')
    
    plt.subplot(312)
    plt.plot(time, acc_y, "r")
    plt.ylabel("Acceleration (milli-g)")
    plt.xlabel("Time (s)")
    plt.legend('Y')
    
    plt.subplot(313)
    plt.plot(time, acc_z, "g")
    plt.xlabel("Time (s)")
    plt.legend('Z')

    plt.show()
    
    
# function: calcTheta
# purpose:  finds the theta values from a given set of accelerations
# paramter: numpy array of accelerations, length of pendulum (float)
# return:   numpy array of angular positions
def calcTheta(accelerations, length):
    accs = accelerations.astype(np.float)
    thetas = np.arctan(np.divide(accs,length))
 
    return scipy.signal.medfilt(thetas)
    
    
# function: graphTheta
# purpose:  takes an array of angular positions and an array of times 
#           and graphs the variables (angular position vs time)
# paramter: numpy array of thetas (radians) of accelerations and numpy of 
#           time (seconds)
# return:   void
def graphTheta(theta, time):
    plt.plot(time, theta, "b")
    plt.ylabel("Angular Position (radians)")
    plt.xlabel("Time (s)")
    plt.title("Pendulum Acceleration vs Time")
    plt.show()
    


# function: displayData
# purpose:  displays accelerations vs time graphs and angle vs time graphs 
#           from the data given, also prints calculated period
# paramter: filename of where data for pendulum is stored (.csv) and string
#           of length of pendulum (inches)
# return:   void
def displayData(file, length):
    print('GETTING DATA FOR PENDULUM WITH LENGTH OF ', length, ' INCHES')
    acc_x = getAccX(file)
    acc_y = getAccY(file)
    acc_z = getAccZ(file)
    time  = getTime(file)
    graphAcc(acc_x,acc_y,acc_z,time)
    thetas = calcTheta(acc_x, float(length))
    graphTheta(thetas,time)
    print('\n\n\n')
    
    
# function: display
# purpose:  displays accelerations vs time graphs and angle vs time graphs 
#           from the data for 5 different length pendulums, also prints 
#           calculated period
# paramter: filenames of where data for each pendulum is stored (.csv)
#           file1 = 21 inches
#           file2 = 17 inches
#           file3 = 13 inches
#           file4 = 9 inches
#           file5 = 4.75 inches 
# return:   void
def display(file1, file2, file3, file4, file5):
    displayData(file1, '21')
    displayData(file2, '17')
    displayData(file3, '13')
    displayData(file4, '9')
    displayData(file5, '4.75')


# MAIN SCRIPT
###################################

#display('Data21.csv', 'Data17.csv', 'Data13.csv', 'Data9.csv', 
#                                                      'Data475.csv')
