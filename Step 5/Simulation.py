# Project 1
# Step 5
# Numerical Simulation Model
# Model.py
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
import math


# GLOBAL VARIABLES
##################################
GRAVITY  = -386.09       #inches/ses/sec
INIT_VEL = 0
INIT_POS = math.pi/4
TIME     = 50           #millisec

# CUSTOM FUNCTION DEFINITIONS
###################################

# function: getInitAcc
# purpose:  finds initial accelertaion given the length of the pendulum
# paramter: length of pendulum (float)
# return:   float (initial acceleration)
def getInitAcc(length):
    return (GRAVITY/length)*math.sin(INIT_POS)


# function: newVel
# purpose:  finds a new angular velocity given an old angular acceleration
# paramter: numpy array of velocities and a numpy array of accelerations
# return:   numpy array of velocities with calculated velocity added
def newVel(accs, vels):
    # old w + acc*t 
    return 0
  
    
# function: newPos
# purpose:  finds a new angular position given an old angular velocity
# paramter: numpy array of velocities and a numpy array of positions
# return:   numpy array of positions with calculated position added
def newPos(vels, pos):
    # old vel*t + pi/4 + (1/2)(g/L sin (old theta) t^2), t = time step
    return 0
    

# function: newAcc
# purpose:  finds a new angular acceleration given an old angular position
# paramter: numpy array of positions and a numpy array of accelerations
# return:   numpy array of accelerations with calculated acceleration added
def newAcc(pos, accs):
    # G/L SIN THETA
    return 0


# function: graphValues
# purpose:  graphs angular accelertaion, velocity , and position over time
# paramter: 4 numpy array of accelerations, velocities, positions, and times
# return:   void
def graphValues(accs, vels, pos, times):
    # TO DO


# MAIN SCRIPT
###################################
for length in [21.0, 17.0, 13.0, 9.0, 4.75]:
    ang_v = [INIT_VEL]
    ang_x = [INIT_POS]
    ang_a = [getInitAcc(length)]
    
    # while loop
    # find new v from last a
    # find new pos from last v
    # find new a form pos
    # graph