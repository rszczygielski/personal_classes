from enum import Enum, auto
from datetime import timedelta
from locale import currency
import random

class BikeType(Enum):
    ROAD_BIKE = auto()
    MOUNTAIN = auto()
    CRUISER = auto()



class Bike_Computer():
    def __init__(self, type):
        self.whole_time = timedelta()
        self.whole_distance = 0
        self.last_distance = 0
        self.time = timedelta()
        self.bikes = [Bike_stats(BikeType.ROAD_BIKE), Bike_stats(BikeType.MOUNTAIN), Bike_stats(BikeType.CRUISER)]
        self.current_bike = self.bikes[0]
        self.type = type


    def set_bike(self, type):
        for bike in self.bikes:
            if type == bike.type:
                self.current_bike = bike
        


    def kmH_to_mS(self, speedkmh):
        return speedkmh * 1000/3600

    def trip(self, time, speed):
        #time - min
        #speed - km/h
        self.time = timedelta(minutes=round(time, 1)) # time
        speed_msh = self.kmH_to_mS(speed)

        self.last_distance = round(self.time.seconds * speed_msh / 1000, 2)
        print(f"****You rode: {self.last_distance} km****")
        print(f"****Time: {self.time} min****")

        """Update of chosen bike"""
        self.current_bike.last_distance = self.last_distance
        self.current_bike.last_time = self.time
        self.current_bike.whole_distance += self.last_distance
        self.current_bike.whole_time += self.time

        """Overall update"""
        self.whole_distance += self.last_distance
        self.whole_time += self.time
    
    def print_last_statistics(self):
        print("\n" + "*" * 25)
        print("*"*8, self.current_bike.type.name , "*"*8)
        print(f"\tLAST RIDE \nDistance: \t{self.last_distance} \nTime: \t\t{self.time}")

    def print_all_statistics(self):
        print("\n" + "*" * 25)
        for bike in self.bikes:
            print("*"*8, bike.type.name, "*"*8)
            print(f"\tWHOLE RIDE \nDistance: \t{bike.whole_distance} \nTime: \t\t{bike.whole_time}")
            print("\n" + "*" * 25)

class Bike_stats():
    def __init__(self, type):
        self.last_distance = 0
        self.last_time = timedelta()
        self.whole_time = timedelta()
        self.whole_distance = 0
        self.type = type


if __name__ == "__main__":
    bike_computer = Bike_Computer(BikeType.ROAD_BIKE)
    for i in range(10):
        bike_computer.trip(random.uniform(1, 100), random.randint(7, 30))
    # bike_computer.print_last_statistics()
    bike_computer.set_bike(BikeType.MOUNTAIN)
    bike_computer.trip(random.uniform(1, 100), random.randint(7, 30))
    bike_computer.print_all_statistics()


    # bike_computer.set_bike(BikeType.BIKE_FIXED)
    # bike_computer.trip(random.uniform(1, 100), random.randint(7, 30))
    # bike_computer.print_last_statistics()
    # bike_computer.print_all_statistics()




#żeby dokładność czasu w sekundach, przełączanie miedzy licznikami, rowery umieścić w liście lub w słowniku, licznik ma typ roweru jako góral, kolarka itp natomiast można wybrać tylko 3 rodzaje rowrów, ile bym spalił jadąc samochodem, maksymalna prędkości z wycieczki, 
# zrobić enum jako typ rowru 
