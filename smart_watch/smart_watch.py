# 3 aktywności, jazda rowerem, spacer, fitnes - każda w innej klasie
import cycling
import fitness
import running
import swimming
import random
from datetime import timedelta

class Smart_watch():
    def __init__(self):
        self.activity_list = []
        self.activity_counter = 0
        self.top_speed = 0
        self.top_distance = 0
        self.top_cals = 0
        self.top_time = timedelta(0,0,0)
        self.full_time = timedelta(0,0,0)

    def aditional_stats_checker(self, speed, distance, cals, time):
        if speed > self.top_speed:
            self.top_speed = speed
        if distance > self.top_distance:
            self.top_distance = distance
        if cals > self.top_cals:
            self.top_cals = cals
        if time > self.top_time:
            self.top_time = time
    
    def adition_stats_printer(self):
        print(("\n" + "*" * 30) * 2 + "\n\t aditional Stats".upper() )
        print(f"\n > Top Speed: {self.top_speed} km/h \n > Top Distance: {self.top_distance} km \n > Cals: {self.top_cals} cal \n > Time: {self.top_time} \n > Full Time: {self.full_time} \n > Activities amount: {self.activity_counter}")
        print(("\n" + "*" * 30) * 2)
        

    def running(self, running:running.Running):
        self.activity_list.append(running)
        self.aditional_stats_checker(running.speed, running.distance, running.cals, running.time)
        self.full_time += running.time
        self.activity_counter += 1


    def fitness(self, fitness:fitness.Fitness):
        self.activity_list.append(fitness)
        self.aditional_stats_checker(0, 0, fitness.cals, fitness.time)
        self.full_time += fitness.time
        self.activity_counter += 1

    def cycling(self, cycling:cycling.Cycling):
        self.activity_list.append(cycling)
        self.aditional_stats_checker(cycling.speed, cycling.distance, cycling.cals, cycling.time)
        self.full_time += cycling.time
        self.activity_counter += 1
    
    def swimming(self, swimming:swimming.Swimming):
        self.activity_list.append(swimming)
        self.aditional_stats_checker(swimming.speed, swimming.distance, swimming.cals, swimming.time)
        self.full_time += swimming.time
        self.activity_counter += 1
    
    
    def activity_printer(self):
        for activity in self.activity_list:
            name = "\n" + ("*" * 30 + "\n") * 2 + "\t" + type(activity).__name__.upper() + "\n"
            if isinstance(activity, fitness.Fitness) == 0:
                common_activites = f" > Speed: {activity.speed} km/h \n > Distance: {activity.distance} km \n > Cals: {activity.cals} cal \n > Time: {activity.time}"
            if isinstance(activity, running.Running):
                print(name)
                print(common_activites)
            if isinstance(activity, cycling.Cycling):
                print(name)
                print(common_activites, f"\n > Bike Type: {activity.type_bike.name}")
            if isinstance(activity, fitness.Fitness):
                print(name)
                print(f"\n > Cals: {activity.cals} cal \n > Time: {activity.time}")
            if isinstance(activity, swimming.Swimming):
                print(name)
                print(common_activites, f"\n > Amount of pools defeted: {activity.pools}")
        print(("\n" + "*" * 30) * 2)


class Simulator():
    @staticmethod
    def kmH_to_mS(speedkmh):
        return speedkmh * 1000/3600
    @staticmethod
    def cycling_sim():
        time = timedelta(seconds=random.randint(1, 10000))
        speed = random.randint(7, 30)
        speed_msh = Simulator.kmH_to_mS(speed)
        distance = round(time.seconds * speed_msh / 1000, 3)
        cals = random.randint(50,2000)
        return cycling.Cycling(speed, distance, cals, time)
    @staticmethod
    def runnin_sim():
        time = timedelta(seconds=random.randint(1, 10000))
        speed = random.randint(5, 15)
        speed_msh = Simulator.kmH_to_mS(speed)
        distance = round(time.seconds * speed_msh / 1000, 3)
        cals = random.randint(50,2000)
        return running.Running(speed, distance, cals, time)
    @staticmethod
    def swimming_sim():
        time = timedelta(seconds=random.randint(1, 10000))
        speed = random.randint(5, 15)
        speed_msh = Simulator.kmH_to_mS(speed)
        distance = round(time.seconds * speed_msh / 1000, 3)
        cals = random.randint(50,2000)
        pools = round(distance % 25)
        return swimming.Swimming(speed, distance, cals, time, pools)
    @staticmethod
    def fitness():
        cals = random.randint(50,2000)
        time = timedelta(seconds=random.randint(1, 10000))
        return fitness.Fitness(cals, time)


""" zmienna statyczna oraz funkcja statyczna jest tlyko jedna i nie wymaga tworzenia instancji""" 

if __name__ == "__main__":
    smart_watch = Smart_watch()
    smart_watch.cycling(Simulator.cycling_sim())
    smart_watch.running(Simulator.runnin_sim())
    smart_watch.swimming(Simulator.swimming_sim())
    smart_watch.swimming(Simulator.swimming_sim())
    smart_watch.fitness(Simulator.fitness())
    smart_watch.activity_printer()
    smart_watch.adition_stats_printer()




## dodać aktywności jakieś, dodatkowo żeby smart watch liczył ile danych aktywności zostało wykonanych, suma czasów wszystkich aktywności, wyświetl rekordowe aktywności


