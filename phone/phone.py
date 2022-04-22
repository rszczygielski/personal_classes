from logger import Logger
import os
# przez to, że w programie logger.py stworzyłem instancje LoggerClass to nie muszę tworzyć podaczas inportu 

class Phone():
    def __init__(self):
        self.contacts = []
        self.nameFile = "contacts.txt"
    
    def AddContact(self, firstName:str, lastName:str, number:int):
        contactFile = open(self.nameFile, "a")
        line = firstName + " " +  lastName + " " + str(number)
        contactFile.write(line)
        contactFile.close()
    
    def ReadContacts(self):
        if not os.path.isfile(self.nameFile):
            Logger.ERROR("There is no such file as contacts.txt")
            return  #w przypadku małego projekstu spoko ale na większa skale może być problem bo ciężko znaleźć taki błąd, ale tutaj dodatkowo mamy loga z errorem
        lines = open(self.nameFile).readlines()
        if len(lines) == 0:
            Logger.WARNING("There is no contacts in file")
        else:
            for line in lines:
                splitedLine = line.split(" ")
                firstName = splitedLine[0]
                lastName = splitedLine[1]
                number = int(splitedLine[2].strip())
                self.contacts.append(Contact(firstName, lastName, number))

class Contact():
    def __init__(self, firstName, lastName, number):
        self.firstName = firstName
        self.lastName = lastName
        self.number = number
            

if __name__ == "__main__":
    phone = Phone()
    phone.ReadContacts()
    phone.AddContact("Radek", "Szczygielski", 668107042)
    phone.ReadContacts()



#  osobna metoda na zapisywanie do pliku oraz usunięnie zapisaywania w addcontact, w addcontacnt dodaje tylko po innym numerze jak istnieje to nie dodaje
#sprawadznie czy numer jest odpowiednio długi, dodawanie numerów do jednej osoby, wyszykujesz kontakty(metoda), szukanie numeru telefony(metoda), sortowanie po imieniu lub nazwisku 