from datetime import timedelta
from time import time


class Swimming():
    def __init__(self, speed=0, distance=0, cals=0, time=timedelta(0,0,0), pools = 0):
        self.speed = speed
        self.distance = distance
        self.cals = cals
        self.time = time
        self.pools = pools