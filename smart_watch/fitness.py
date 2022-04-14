from datetime import timedelta

class Fitness():
    def __init__(self, cals=0, time=timedelta(0,0,0)):
        self.cals = cals
        self.time = time