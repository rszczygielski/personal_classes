# 3 aktywności, jazda rowerem, spacer, fitnes - każda w innej klasie
import cycling
import fitness
import running
import random
from datetime import timedelta

class Smart_watch():
    def __init__(self):
        self.activity_list = []

    def running(self, running:running.Running):
        self.activity_list.append(running)

    def fitness(self, fitness:fitness.Fitness):
        self.activity_list.append(fitness)

    def cycling(self, cycling:cycling.Cycling_activity):
        self.activity_list.append(cycling)
    
    def activity_printer(self):
        for activity in self.activity_list:
            if isinstance(activity, running.Running):
                print(activity.speed, activity.distance, activity.cals, activity.time)
            if isinstance(activity, cycling.Cycling_activity):
                print(activity.speed, activity.distance, activity.cals, activity.time, activity.type_bike.name)
            if isinstance(activity, fitness.Fitness):
                print(activity.cals, activity.time)


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
        return cycling.Cycling_activity(speed, distance, cals, time)
    @staticmethod
    def runnin_sim():
        time = timedelta(seconds=random.randint(1, 10000))
        speed = random.randint(5, 15)
        speed_msh = Simulator.kmH_to_mS(speed)
        distance = round(time.seconds * speed_msh / 1000, 3)
        cals = random.randint(50,2000)
        return running.Running(speed, distance, cals, time)

""" zmienna statyczna oraz funkcja statyczna jest tlyko jedna i nie wymaga tworzenia instancji""" 

if __name__ == "__main__":
    smart_watch = Smart_watch()
    smart_watch.cycling(Simulator.cycling_sim())
    smart_watch.running(Simulator.runnin_sim())
    smart_watch.activity_printer()




## dodać aktywności jakieś, dodatkowo żeby smart watch liczył ile danych aktywności zostało wykonanych, suma czasów wszystkich aktywności, wyświetl rekordowe aktywności


