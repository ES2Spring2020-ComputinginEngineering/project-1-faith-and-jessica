# Project 1
# Step 4
# Analysis of Results
# Period.py
#
# Jessica Nordlund 
# Faith Seely
# 
##################################

# IMPORT STATEMENTS
##################################
import numpy as np
import Graphs
import matplotlib.pyplot as plt


# CUSTOM FUNCTION DEFINITIONS
###################################

# function: calcPeriod
# purpose:  finds the period of the pendulum
# paramter: numpy array of accelerations and numpy array of times 
# return:   float (calculated period)
def calcPeriod(angles, times):
    periods = np.empty(0, dtype=float)
    last_p  = 0
    
    for i in range(1,len(angles)):
        if (angles[i-1] > 0 and angles[i] < 0):
            new_p   = (times[i-1] + times[i])/2
            periods = np.append(periods, new_p - last_p)
            last_p  = new_p
            
    avg_period = 0
    for elem in periods:
        avg_period = avg_period + elem
        
    return avg_period / len(periods)


# function: calcAllPeriods
# purpose:  finds the period of the pendulums from the given files
# paramter: file names
#           file1 = 21 inches
#           file2 = 17 inches
#           file3 = 13 inches
#           file4 = 9 inches
#           file5 = 4.75 inches 
# return:   array of periods (floats)
def calcAllPeriods(file1, file2, file3, file4, file5):
    acc21 = Graphs.getAccX(file1)
    ang21 = Graphs.calcTheta(acc21,float(21))
    time21 = Graphs.getTime(file1)
    period21 = calcPeriod(ang21,time21)
    print('Calculated period of pendulum with length of 21 inches: ', period21)

    acc17 = Graphs.getAccX(file2)
    ang17 = Graphs.calcTheta(acc17,float(17))
    time17 = Graphs.getTime(file2)
    period17 = calcPeriod(ang17,time17)
    print('Calculated period of pendulum with length of 17 inches: ', period17)

    acc13 = Graphs.getAccX(file3)
    ang13 = Graphs.calcTheta(acc13,float(13))
    time13 = Graphs.getTime(file3)
    period13 = calcPeriod(ang13,time13)
    print('Calculated period of pendulum with length of 13 inches: ', period13)
    
    acc9 = Graphs.getAccX(file4)
    ang9 = Graphs.calcTheta(acc9,float(9))
    time9 = Graphs.getTime(file4)
    period9 = calcPeriod(ang9,time9)
    print('Calculated period of pendulum with length of 9 inches: ', period9)
    
    acc5 = Graphs.getAccX(file5)
    ang5 = Graphs.calcTheta(acc5,float(4.75))
    time5 = Graphs.getTime(file5)
    period5 = calcPeriod(ang5,time5)
    print('Calculated period of pendulum with length of 4.75 inches:', period5)
    
    return [period21, period17, period13, period9, period5]


# function: graphPvL
# purpose:  graphs period vs length of pendulums
# paramter: numpy array of periods and corresponding lengths
# return:   void
def graphPvL(periods, lengths):
    plt.plot(lengths, periods, "b")
    plt.ylabel("Period (s)")
    plt.xlabel("Length (inches)")
    plt.title("Pendulum Period vs Length")
    plt.show()
    
# function: graphLog
# purpose:  takes an array of lengths and an array of periods of a pendulum 
#           and graphs the logs of these arrays
# paramter: numpy array of lengths of pendulum and numpy of periods
# return:   void
def graphLog(lens, periods):
    plt.plot(lens, periods, "-bo")
    plt.xlabel("Length (inches)")
    plt.ylabel("Period (s)")
    plt.title("Pendulum Period vs Length (log scale)")
    plt.yscale('log')
    plt.xscale('log')
    plt.show()

    
# MAIN SCRIPT
###################################
periods = calcAllPeriods('Data21.csv', 'Data17.csv', 'Data13.csv', 
                                       'Data9.csv' , 'Data475.csv')
lengths = [21.0, 17.0, 13.0, 9.0, 4.75]
graphPvL(periods, lengths)
graphLog(lengths, periods)