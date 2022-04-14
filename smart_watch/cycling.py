from datetime import timedelta
from enum import Enum, auto

class BikeType(Enum):
    UNIVERSAL = auto()
    MOUNTAIN = auto()
    CRUISER = auto()


class Cycling_activity():
    def __init__(self, speed=0, distance=0, cals=0, time=timedelta(0,0,0), type_bike=BikeType.UNIVERSAL):
        self.speed = speed
        self.distance = distance
        self.cals = cals
        self.time = time
        self.type_bike = type_bike








    
