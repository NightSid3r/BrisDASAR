import sys
sys.path.append( './bin')

from drones import Drone
import numpy as np

x = np.linspace(-3,3,50)
y=x

ActiveDrones={}
NumDrones=4
for jj in range(0,NumDrones):
    ActiveDrones[jj]=Drone()
    print(ActiveDrones[jj])

ActiveDrones[1].initialSetup("Camera",[1,2])

ActiveDrones[1].setCurrentLocation([2,2])
ActiveDrones[1].setCurrentLocation([3,2])
ActiveDrones[1].getPreviousLocations()