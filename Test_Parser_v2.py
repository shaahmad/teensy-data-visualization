#Jaehwan Lee, Ocober 2015

import matplotlib.pyplot as plt
import numpy as np
import sys
import time

startTime = time.time() #For real time graph

#Data Storage
Data = ' '
inChar = ' '

#For Test
TestArray = np.random.randint(0, 1000, size = 1000)
indx = 0;

t = startTime-time.time() #Time since start

plt.figure() #Creating Figure
plt.ylabel("Angle", fontsize=20)
plt.xlabel("Time", fontsize=20)
plt.grid(True)
plt.axis([0, 15, 0, 1000]) # Axis Ranges
plt.ion() #interactive mode on
line, = plt.plot([], [])
plt.show(block=False) #Show graph

#graphing
while True:
        t = time.time() - startTime #keeping track of time
        line.set_xdata(np.append(line.get_xdata(), t))
        line.set_ydata(np.append(line.get_ydata(), TestArray[indx]))
        plt.draw()
        indx += 1
        if t>15: #Axis Reset
            plt.cla() #clear axis
            plt.axis([0, 15, 0, 1000]) #Resetting the axis
            plt.grid(True)
            plt.ylabel("Angle", fontsize=20)
            plt.xlabel("Time", fontsize=20)
            line, = plt.plot([], [])
            startTime = time.time() #go back to time 0
        plt.pause(0.01)
