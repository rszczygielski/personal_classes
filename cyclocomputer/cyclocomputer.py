from enum import Enum, auto
from datetime import timedelta
import random

class BikeType(Enum):
    ROAD_BIKE = auto
    MOUNTAIN = auto
    BIKE_FOLDING = auto
    BIKE_FIXED = auto
    GEAR_BIKE = auto
    BMX = auto
    RECUMBENT_BIKE = auto
    CRUISER = auto



class Bike_Computer():
    def __init__(self):
        self.whole_time = timedelta()
        self.whole_distance = 0
        self.last_distance = 0
        self.time = timedelta()
        self.bikes = [Bike_stats(), Bike_stats(), Bike_stats()]
        self.current_bike = self.bikes[0]
        self.types = ["Road Bike", "Mountain", "Bike.Touring", "Bike.Folding", "Bike.Fixed Gear/Track Bike", "BMX", "Recumbent Bike", "Cruiser"]

    def chose_bike(self):
        bike_number = input("""
        Press 1 to chose bike1
        Press 2 to chose bike2
        Press 3 to chose bike3: """)
        if bike_number == "1":
            self.current_bike = self.bikes[0]
        if bike_number == "2":
            self.current_bike = self.bikes[1]
        if bike_number == "3":
            self.current_bike = self.bikes[2]
    
    def change_type_of_bike(self):
        chose_bike_type = int(input("""
        Chose bike type from the list to assign it to the current bike
        1.Road Bike 
        2.Mountain Bike 
        3.Touring Bike 
        4.Folding Bike
        5.Fixed Bike
        6.Gear/Track Bike 
        7.BMX 
        8.Recumbent Bike 
        9.Cruiser"""))
        self.current_bike.type = self.types[chose_bike_type - 1]
        
        
        
    def kmH_to_mS(self, speedkmh):
        return speedkmh * 1000/3600

    def trip(self, time, speed):
        #time - min
        #speed - km/h
        self.time = timedelta(minutes=round(time, 1)) # czas
        speed_msh = self.kmH_to_mS(speed)

        self.last_distance = round(self.time.seconds * speed_msh / 1000, 2)
        print(f"You rode: {self.last_distance} km")
        print(f"Time: {self.time} min")

        """Update of chosen bike"""
        self.current_bike.last_distance = self.last_distance
        self.current_bike.last_time = self.time
        self.current_bike.whole_distance += self.last_distance
        self.current_bike.whole_time += self.time

        """Overall update"""
        self.whole_distance += self.last_distance
        self.whole_time += self.time
    
    def print_statististics(self):
        menu = input("""
        Press 1 to print stats ralated to bike 1
        Press 2 to print stats ralated to bike 2
        Press 3 to print stats ralated to bike 3
        Press 4 to print statictisc for last ride
        Press 5 to print sum statistics: """)

        if menu == "1":
            print(f"""
        {self.bikes[0].type}
        Last distance of bike 1: {self.bikes[0].last_distance}
        Last time of ride of bike 1: {self.bikes[0].last_time}
        Whole distance of bike 1: {self.bikes[0].whole_distance}
        Whole time of bike 1: {self.bikes[0].whole_time}""")
        if menu == "2":
            print(f"""
        {self.bikes[1].type}
        Last distance of bike 2: {self.bikes[1].last_distance}
        Last time of ride of bike 2: {self.bikes[1].last_time}
        Whole distance of bike 2: {self.bikes[1].whole_distance}
        Whole time of bike 2: {self.bikes[1].whole_time}""")
        if menu == "3":
            print(f"""
        {self.bikes[2].type}
        Last distance of bike 3: {self.bikes[2].last_distance}
        Last time of ride of bike 3: {self.bikes[2].last_time}
        Whole distance of bike 3: {self.bikes[2].whole_distance}
        Whole time of bike 3: {self.bikes[2].whole_time}""")

        if menu == "4":
            print(f"""
            Last ride
            Distance: {self.last_distance}
            Time: {self.time}""")
        if menu == "5":
            print(f"""
            Whole distance: {self.whole_distance} 
            Whole time: {self.whole_time}""")
        

class Bike_stats():
    def __init__(self):
        self.last_distance = 0
        self.last_time = timedelta()
        self.whole_time = timedelta()
        self.whole_distance = 0
        self.type = ""


if __name__ == "__main__":
    bike_computer = Bike_Computer()
    bike_computer.chose_bike()
    bike_computer.change_type_of_bike()


    for _ in range(10):
        bike_computer.trip(random.uniform(1, 100), random.randint(7, 30))
    for _ in range(3):
        bike_computer.print_statististics()


    bike_computer.chose_bike()
    bike_computer.change_type_of_bike()
    for _ in range(10):
        bike_computer.trip(random.uniform(1, 100), random.randint(7, 30))
    for _ in range(3):
        bike_computer.print_statististics()

    
    bike_computer.chose_bike()
    bike_computer.change_type_of_bike()
    for _ in range(10):
        bike_computer.trip(random.uniform(1, 100), random.randint(7, 30))
    for _ in range(3):
        bike_computer.print_statististics()
    




#??eby dok??adno???? czasu w sekundach, prze????czanie miedzy licznikami, rowery umie??ci?? w li??cie lub w s??owniku, licznik ma typ roweru jako g??ral, kolarka itp natomiast mo??na wybra?? tylko 3 rodzaje rowr??w, ile bym spali?? jad??c samochodem, maksymalna pr??dko??ci z wycieczki, 
# zrobi?? enum jako typ rowru 
