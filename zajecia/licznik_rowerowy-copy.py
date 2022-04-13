from enum import Enum, auto
from datetime import timedelta
import random

class BikeType(Enum):
    ROAD_BIKE = auto()
    MOUNTAIN = auto()
    BIKE_FOLDING = auto()
    BIKE_FIXED = auto()
    GEAR_BIKE = auto()
    BMX = auto()
    RECUMBENT_BIKE = auto()
    CRUISER = auto()



class Bike_Computer():
    def __init__(self, type):
        self.whole_time = timedelta()
        self.whole_distance = 0
        self.last_distance = 0
        self.time = timedelta()
        self.bikes = [Bike_stats(), Bike_stats(), Bike_stats()]
        self.current_bike = self.bikes[0]
        self.type = type.name

    
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
        print("*****", self.type , "*****")
        print(f"\tLAST RIDE \n\tDistance: {self.last_distance} \n\tTime: {self.time}")

    def print_all_statistics(self):
        print(f"""
            Whole distance: {self.whole_distance} 
            Whole time: {self.whole_time}""")

class Bike_stats():
    def __init__(self):
        self.last_distance = 0
        self.last_time = timedelta()
        self.whole_time = timedelta()
        self.whole_distance = 0


if __name__ == "__main__":
    bike_computer = Bike_Computer(BikeType.CRUISER)
    bike_computer.trip(random.uniform(1, 100), random.randint(7, 30))
    bike_computer.print_last_statistics()




#żeby dokładność czasu w sekundach, przełączanie miedzy licznikami, rowery umieścić w liście lub w słowniku, licznik ma typ roweru jako góral, kolarka itp natomiast można wybrać tylko 3 rodzaje rowrów, ile bym spalił jadąc samochodem, maksymalna prędkości z wycieczki, 
# zrobić enum jako typ rowru 
