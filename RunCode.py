import sys
sys.path.append( './bin')
sys.path.append( './GUI')

from drones import Drone
import dasarFunc
import numpy as np


Dronexcurrent = np.ones((1,2))
Droneycurrent = np.ones((1,2))
    
select = 0

numCells = 50

drone_alt = 0
pathsmoothing = 0
showsteps=1

x = np.linspace(-3,3,50)
y=x
for N in range(0,)
targety, targetx = dasarFunc.randompoints(N)

ActiveDrones={}
NumDrones=4
for jj in range(0,NumDrones):
    ActiveDrones[jj]=Drone()
    print(ActiveDrones[jj])

ActiveDrones[1].initialSetup("Camera",[1,2])

ActiveDrones[1].setCurrentLocation([2,2])
ActiveDrones[1].setCurrentLocation([3,2])
ActiveDrones[1].getPreviousLocations()