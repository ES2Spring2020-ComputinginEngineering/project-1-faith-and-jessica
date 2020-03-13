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
import matplotlib.pyplot as plt
import math
import time


# GLOBAL VARIABLES
##################################
GRAVITY   = -386.09             #inches/ses/sec
INIT_VEL  = 0
INIT_POS  = math.pi/4
TIME      = 2                   #seconds

# CUSTOM FUNCTION DEFINITIONS
###################################

# function: getInitAcc
# purpose:  finds initial accelertaion given the length of the pendulum
# paramter: length of pendulum (float)
# return:   float (initial acceleration)
def getInitAcc(length):
    return (GRAVITY/length)*math.sin(INIT_POS)


# function: newTime
# purpose:  adds a new time in seconds to the given array and returns new 
# paramter: numpy array of times
# return:   modified numpy array of times
def newTime(times):
    return np.append(times, time.time())

# function: newVel
# purpose:  finds a new angular velocity given an old angular acceleration
# paramter: 3 numpy arrays of velocities, accelerations, and times
# return:   numpy array of velocities with calculated velocity added
def newVel(accs, vels, times):
    # old w + acc*t 
    time_elapsed = times[len(times)-1] - times[len(times)-2]
    new_vel = vels[len(vels)-1] + (accs[len(accs)-1] * time_elapsed)
    return np.append(vels,new_vel)
    
  
    
# function: newPos
# purpose:  finds a new angular position given an old angular velocity
# paramter: 3 numpy array of velocities, positions, and times and length of 
#           pendulum
# return:   numpy array of positions with calculated position added
def newPos(vels, pos, times, length):
    # old pos + old vel*t + (1/2)(g/L sin (old theta) t^2), t = time step
    time_elapsed = times[len(times)-1] - times[len(times)-2]
    term1  = vels[len(vels)-1]
    term2 = (1/2)*(GRAVITY/length)*(math.sin(pos[len(pos)-1]))
    new_pos = pos[len(pos)-1] + term1*time_elapsed + term2*(time_elapsed**2)
    return np.append(pos,new_pos)
    

# function: newAcc
# purpose:  finds a new angular acceleration given an old angular position
# paramter: numpy array of positions and a numpy array of accelerations and 
#           the length of the pendulum
# return:   numpy array of accelerations with calculated acceleration added
def newAcc(pos, accs, times, length):
    # G/L SIN THETA
    new_acc = (GRAVITY/length) * math.sin(pos[len(pos)-1])
    return np.append(accs,new_acc)

# function: normalizeTimes
# purpose:  takes the times numpy array and scales it to start at 0     
# paramter: numpy array of times
# return:   modified numpy array of times
def normalizeTimes(times):
    np_len = len(times)
    result = [0]
    temp   = times[0]
    
    for i in range(1,np_len-1):
        new_t  = (times[i] - temp) + result[i-1]
        temp   = times[i]
        result = np.append(result,new_t)
        
    return result


# function: graphValues
# purpose:  graphs angular accelertaion, velocity , and position over time
# paramter: 4 numpy array of accelerations, velocities, positions, and times
# return:   void
def graphValues(accs, vels, pos, times):
    plt.plot(times, accs, "b")
    plt.xlabel("Time (s)")
    plt.ylabel("Angular Accleration (radians/s^2)")
    plt.title("Pendulum Acceleration vs Time")
    plt.show()
    
    plt.plot(times, vels, "r")
    plt.xlabel("Time (s)")
    plt.ylabel("Angular Velocity (radians/sec)")
    plt.title("Pendulum Velocity vs Time")
    plt.show()
    
    plt.plot(times, pos, "g")
    plt.xlabel("Time (s)")
    plt.ylabel("Angular Position (radians)")
    plt.title("Pendulum Position vs Time")
    plt.show()


# function: calcPeriod
# purpose:  finds the period of the pendulum
# paramter: numpy array of angles and numpy array of times 
# return:   float (calculated period)
def calcPeriod(angles, times):
    periods = np.empty(0, dtype=float)
    last_p  = 0
    
    for i in range(1,len(angles)):
        #check conditional
        if (angles[i-1] > 0 and angles[i] < 0):
            new_p   = (times[i-1] + times[i])/2
            periods = np.append(periods, new_p - last_p)
            last_p  = new_p
            
    avg_period = 0
    for elem in periods:
        avg_period = avg_period + elem

    return avg_period / len(periods)



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
    

# MAIN SCRIPT
###################################
periods = []
lengths = np.array([21.0, 17.0, 13.0, 9.0, 4.75])

for length in lengths:
    times = [time.time()]
    ang_v = [INIT_VEL]
    ang_x = [INIT_POS]
    ang_a = [getInitAcc(length)]
    
    elapsed_time = 0
    
    while (elapsed_time < TIME):
        times = newTime(times)
        ang_v = newVel(ang_a,ang_v,times)
        ang_x = newPos(ang_v,ang_x,times,length)
        ang_a = newAcc(ang_x,ang_a,times,length)
        
        elapsed_time = time.time() - times[0]
    
    #scale time
    times = normalizeTimes(times)
    
    #make arrays the same shape
    times = times[:30000]
    ang_a = ang_a[:30000]
    ang_v = ang_v[:30000]
    ang_x = ang_x[:30000]
    graphValues(ang_a,ang_v,ang_x,times)
    
    periods = np.append(periods,calcPeriod(ang_x,times))


graphPvL(periods,lengths)