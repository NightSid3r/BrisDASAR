class Drone():
    def __init__(self):
        self.droneType=None
        self.droneCurrentLocation=[]
        self.droneAltitude=None
        self.droneManualControl=None
        self.dronePreviousLocations=[]
    
    def initialSetup(self, drone_type, current_location, altitude=120, manual_control=False):
        self.droneType=drone_type
        self.droneCurrentLocation=current_location
        self.droneAltitude=altitude
        self.droneManualControl=manual_control
        self.dronePreviousLocations.append(current_location)
    
    def setCurrentLocation(self,current_location):
        self.droneCurrentLocation=current_location
        self.dronePreviousLocations.append(self.droneCurrentLocation)
    
    def getPreviousLocations(self):
        return(self.dronePreviousLocations)