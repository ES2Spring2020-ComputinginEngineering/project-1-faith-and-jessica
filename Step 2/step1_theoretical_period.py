# Project 1
# Step 2
# Theoretical Based Equation Model
#
# Jessica Nordlund 
# Faith Seely
#
#
# While this model follows the theoretical equation T = 2pi(L/g)^1/2, this 
# equation does not account for friction or air resistance. It also assumes 
# all the mass of the pendulum is at the end of the string when in reality the
# string also has mass and its own gravitational pull. This means that the 
# model can only be so accurate and does not fully represent the real pendulum 
# we built.
# 
##################################

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
    plt.plot(periods, lens, "-bo")
    plt.ylabel("Length (inches)")
    plt.xlabel("Period (s)")
    plt.title("Pendulum Length vs Period")
    plt.show()

# MAIN SCRIPT
###################################
lengths = np.array([5,9,13,17,21])
periods = estimatedPeriod(lengths)
graphValues(lengths,periods)
print("Estimated periods (s): ")
print(periods)