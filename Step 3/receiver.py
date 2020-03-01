##################
# Project 1
# Step 3
# Receiver.py
#
#
# Jessica Nordlund
# Faith Seely
#################

import microbit as mb
import radio  # Needs to be imported separately
import os

path='C:/users/draw6/documents/github/project-1-faith-and-jessica/Step 3'
os.chdir(path)  #Error saying that 'chdir' is not an attribute of 'module'

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=5, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)

fout = open('pendulum.txt', 'w')
print("file opened")
# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')


while True:
    incoming = radio.receive() # Read from radio

    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)

        #############################################################
        # FILL IN HERE
        # Incoming is string sent from logger
        # Need to parse it and reformat as a tuple for the MU plotter
        #############################################################
        info = incoming.split()
        for elem in info:
            fout.write(elem)
            print("element added to text file")
            fout.write(' ')
        fout.write('\n')


        tup1 = float(info[0])
        tup2 = float(info[1])
        tup3 = float(info[2])
        tup4 = float(info[3])/1000

        data = (tup1, tup2, tup3, tup4)
        print(data)

        mb.sleep(100)

    fout.close()