import argparse
from datetime import timedelta
from enum import Enum, auto
import random
import os


class BikeType(Enum):
    ROAD_BIKE = auto()
    MOUNTAIN = auto()
    BIKE_FOLDING = auto()
    BIKE_FIXED = auto()
    GEAR_BIKE = auto()
    BMX = auto()
    RECUMBENT_BIKE = auto()
    CRUISER = auto()


class Test():
    def __init__(self, type):
        self.type = type


    def printer(self):
        print(self.type.name)
# # def printer(x):
# #     return x

# # d = {"a": 1, "b": 2, "c": 3}
# # L = ["a","v", "x", 1, 2, 3]
# # x = "string"
# # d = {"a": 1, "b": 2, "c": 3, "d": 4}
# # # print(printer(d))
# # # print(printer(L))
# # # print(printer(x))


# # def adder(*arg):
# #     sum = arg[0]
# #     for elem in arg[1:]:
# #         sum = sum + elem 
# #     return sum
# # # print(adder(x,x))
# # # print(adder(1,2,3 ))
# # # print(adder(1,5))

# # def copy_dict(dict, dict2):
# #     dictionary_cop = {}
# #     for key in dict:
# #         dictionary_cop[key] = dict[key]

# #     for key_2 in dict2:
# #         if key_2 in dictionary_cop:
# #             continue
# #         else:
# #             dictionary_cop[key_2] = dict2[key_2]
# #     return dictionary_cop

# # # print(copy_dict(d,d))

# # import mymod
# # from mymod import test
# # mymod.test
# # import datetime
# # zmienna = [1, 5, 2011]

# from itertools import count
# import statistics
# from encodings import utf_8
# from posixpath import split
# import datetime


# def read_films(name_file: str):
#     films = []
#     with open(name_file, encoding="utf-8") as file:
#         film = {}
#         for line in file.readlines():
#             line = line.strip()
#             if ":" in line:
#                 f = line.split(":")
#                 if "rating" in line:
#                     film[f[0]] = float(f[1])
#                 else:
#                     film[f[0]] = f[1]
#             else:
#                 films.append(film)
#                 film = {}
#     return films
 
# parser = argparse.ArgumentParser(description='program which returns an square')
# parser.add_argument('s1', metavar='side1', type=int,
#                 help='This represents side1' )
# parser.add_argument('s2', metavar='side2', type=int,
#                 help='This represents side2')
# args = parser.parse_args()

# def square (side1, side2):
#     return 2 * (side1 + side2)

def command():
    return os.system("hmmbuild -h")

if __name__ == "__main__":
    # print (square(args.s1, args.s2))
    # bike = Test(BikeType.BIKE_FIXED) 
    # bike.printer()
    path = os.getcwd()
    name = input("Chose file name: ")
    file1 = open(path+"/"+name+".txt", "w")
    file1.write("\033[93m" + "WARNING" +"\033[0m")
    # command()
    

    
