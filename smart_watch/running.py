from datetime import timedelta


class Running():
    def __init__(self, speed=0, distance=0, cals=0, time=timedelta(0,0,0)):
        self.speed = speed
        self.distance = distance
        self.cals = cals
        self.time = time