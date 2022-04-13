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
            rating = float()
            premiere = datetime.date(1999, 1, 29)
            title = ""
            production = ""
            type = ""
            for line in file.readlines():
                line = line.strip()
                if ":" in line:
                    splited_line = line.split(":")
                    value_name = splited_line[1]
                    if "rating" in line:
                        rating = float(value_name)
                    elif "premiere" in line:
                        date_string = value_name.split(".")
                        premiere = datetime.date(int(date_string[2]), int(date_string[1]), int(date_string[0]))
                    elif "title" in line:
                        title = value_name
                    elif "production" in line:
                        production = value_name
                    elif "type" in line:
                        type = value_name
                self.films.append(Movie(title, rating, type, production, premiere))
               
                
    def printer(self):
        for elm in self.films:
            print(elm)


    def names_of_films(self):
        for movie in self.films:
            print(movie.title)

    def best_rate(self):
        rates = []
        for movie in self.films:
            rates.append(movie.rating)
        best = max(rates)
        print(rates)
        for movie in self.films:
            if movie.rating == best:
                print(movie.title)
        
    def median_comedy(self):
        rates = []
        for movie in self.films:
            if "Comedy" in movie.type:
                rates.append(movie.rating)
        suma = 0
        for rate in rates:
            suma += rate
        print(suma / len(rates))

    def newest_film(self):
        film_name = self.films[0].title
        date_p = self.films[0].premiere
        for movie in self.films:
            chacked_date = movie.premiere
            if chacked_date > date_p:
                film_name = movie.title
                date_p = chacked_date
        print(film_name, date_p)

    def film_finder(self):
        name = input("Chose a film: ")
        for movie in self.films:
            if name in movie.title:
                print(movie.title, "\n", movie.rating, "\n", movie.type, "\n", movie.production, "\n", movie.premiere)
                return 
        print("There is no such a movie on a list. Try again")

    def best_rate_comedy(self):
        rates = []
        for movie in self.films:
            if "comedy" in movie.type.lower():
                rates.append(movie.rating)
        best_rate = max(rates)
        for movie in self.films:
            if movie.rating == best_rate :
                if "comedy" in movie.type.lower():
                    print(movie.title)
        

    def type_conter(self):
        types = []
        for movie in self.films:
            if movie.type not in types:
                types.append(movie.type)
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

class Movie():
    def __init__(self, title, rating, type, production, premiere):
        self.title = title
        self.rating = rating
        self.type = type
        self.production = production
        self.premiere = premiere
    





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
    klasa = FilmSorter("filmweb.txt")

    
