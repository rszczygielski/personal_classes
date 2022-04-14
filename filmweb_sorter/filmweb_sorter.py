from itertools import count
import statistics
from encodings import utf_8
from posixpath import split
import datetime

class FilmSorter():
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.films = []
        self.read_films()

    def read_films(self):
        with open(self.file_name, encoding="utf-8") as file:
            film = {}
            for line in file.readlines():
                line = line.strip()
                if ":" in line:
                    splited_line = line.split(":")
                    key_name = splited_line[0]
                    value_name = splited_line[1]
                    if "rating" in line:
                        film[key_name] = float(value_name)
                    elif "premiere" in line:
                        date_string = value_name.split(".")
                        film[key_name] = datetime.date(int(date_string[2]), int(date_string[1]), int(date_string[0]))
                    else:
                        film[key_name] = value_name
                else:
                    self.films.append(film)
                    film = {}
    

    def names_of_films(self):
        for dict in self.films:
            print(dict["title"])

    def best_rate(self):
        rates = []
        for dict in self.films:
            rates.append(dict["rating"])
        best = max(rates)
        print(rates)
        for dict in self.films:
            if dict["rating"] == best:
                print(dict["title"])
        
    def median_comedy(self):
        rates = []
        for dict in self.films:
            if "Comedy" in dict["type"]:
                rates.append(dict["rating"])
        suma = 0
        for rate in rates:
            suma += rate
        print(suma / len(rates))

    def newest_film(self):
        film_name = self.films[0]["title"]
        date_p = self.films[0]["premiere"]
        for dict in self.films:
            chacked_date = dict["premiere"]
            if chacked_date > date_p:
                film_name = dict['title']
                date_p = chacked_date
        print(film_name, date_p)

    def film_finder(self):
        name = input("Chose a film: ")
        for dict in self.films:
            if name == dict["title"]:
                print(dict)
                return 
        print("There is no such a movie on a list. Try again")

    def best_rate_comedy(self):
        rates = []
        for dict in self.films:
            if "comedy" in dict["type"].lower():
                rates.append(dict["rating"])
        best_rate = max(rates)
        for dict in self.films:
            if dict["rating"] == best_rate :
                if "comedy" in dict["type"].lower():
                    print(dict["title"])
        

    def type_conter(self):
        types = []
        for dict in self.films:
            if dict["type"] not in types:
                types.append(dict["type"])
        print(types, f"There are {len(types)} movie types on that list")

def run(file_name):
    film_sorter = FilmSorter(file_name)
    number = input("""
        Press 1 to read all filmes with data
        Press 2 to print names of all movies on the list
        Press 3 to find a movie with best rating
        Press 4 to print a median of comedy rates
        Press 5 to print the newest film
        Press 6 to search for a movie
        Press 7 to find comedy with the best rating
        Press 8 to print all types of movies on the list: """)

    if number == "1":
        film_sorter.names_of_films()
    elif number == "2":
        film_sorter.names_of_films()
    elif number == "3":
        film_sorter.best_rate()
    elif number == "4":
        film_sorter.median_comedy()
    elif number == "5":
        film_sorter.newest_film()
    elif number == "6":
        film_sorter.film_finder()
    elif number == "7":
        film_sorter.best_rate_comedy()
    elif number == "8":
        film_sorter.type_conter()
    else:
        print("Please enter the correct number")


if __name__ == "__main__":
    # print(read_films("filmweb.txt"))
    # for element in read_films("filmweb.txt"):
    #     print(element)
    # names_of_films(read_films("filmweb.txt"))
    # best_rate((read_films("filmweb.txt")))
    # median_comedy(read_films("filmweb.txt"))
    # newest_film(read_films("filmweb.txt"))
    # film_finder((read_films("filmweb.txt")))
    # best_rate_comedy((read_films("filmweb.txt")))
    # type_conter((read_films("filmweb.txt")))
    run("filmweb.txt")
