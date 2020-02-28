# Project 1
# Step 2
# Theoretical Based Equation Model

# IMPORT STATEMENTS
##################################
import math
import numpy as np
import matplotlib.pyplot as plt

# GLOBAL VARIABLES
###################################
GRAVITY = 386.09 #inches/ses/sec

# CUSTOM FUNCTION DEFINITIONS
###################################

# function: estimatePeriod
# purpose:  takes an array of lengths of a pendulum and returns array of 
#           estimated periods based on the equation T = 2pi(L/g)^1/2
# paramter: numpy array of lengths of pendulum
# return:   array of estimated periods of the different pendulums (seconds)
def estimatedPeriod(lens):
    result = np.sqrt(lens / GRAVITY)
    result = result * math.pi * 2
    return result

# function: graphValues
# purpose:  takes an array of lengths and an array of periods of a pendulum 
#           and graphs the variables (lengths vs periods)
# paramter: numpy array of lengths of pendulum and numpy of periods
# return:   void
def graphValues(lens, periods):
    plt.plot(periods, lens, "ro")
    plt.ylabel("Length (inches)")
    plt.xlabel("Period (s)")
    #plt.axis(0,15,0,22)
    plt.show()

# MAIN SCRIPT
###################################
lengths = np.array([5,9,13,17,21])
periods = estimatedPeriod(lengths)
graphValues(lengths,periods)