from logger import Logger
from enum import Enum, auto
import os
# przez to, że w programie logger.py stworzyłem instancje LoggerClass to nie muszę tworzyć podaczas inportu 

class NumberType(Enum):
        WORK = auto
        FAX = auto
        PERSONAL = auto
        MOBILE = auto
        HOME = auto

class Phone():
    def __init__(self):
        self.contacts = []
        self.nameFile = "contacts.txt"

    
    def AddContact(self, firstName:str, lastName:str, *numbers):
        for newNumber in numbers:
            if len(newNumber) != 9:
                Logger.ERROR("It is not a correct number")
                return
            for contact in self.contacts:
                if newNumber in contact.numbers:
                    Logger.ERROR("This numbers already exists")
                    return                
        self.contacts.append(Contact(firstName, lastName, numbers))
        
    
    def SaveFile(self):
        contactFile = open(self.nameFile, "a")
        for contatct in self.contacts:
            numbers = ""
            for number in contatct.numbers:
                numbers += number + " "
            line = contatct.firstName + " " + contatct.lastName + " "  + numbers + "\n"
            contactFile.write(line)
        contactFile.close()
    
    def IfDuplicatesExsist(self, firstName:str, lastName:str, numbers):
        for contact in self.contacts:
            for number in contact.numbers:
                if contact.firstName == firstName and contact.lastName == lastName and number not in numbers:
                    return True
        return False

    def ReadContacts(self):
        if not os.path.isfile(self.nameFile):
            Logger.WARNING("There is no such file as contacts.txt")
            return  #w przypadku małego projekstu spoko ale na większa skale może być problem bo ciężko znaleźć taki błąd, ale tutaj dodatkowo mamy loga z errorem
        lines = open(self.nameFile).readlines()
        if len(lines) == 0:
            Logger.WARNING("There is no contacts in file")
        else:
            for line in lines:
                splitedLine = line.split(" ")
                if len(splitedLine) >= 3:
                    firstName = splitedLine[0]
                    lastName = splitedLine[1]
                    numbers = splitedLine[2:]
                    numbers = numbers[-1].strip()
                    if not self.IfDuplicatesExsist(firstName, lastName, numbers):
                        self.contacts.append(Contact(firstName, lastName, numbers))
            for contact in self.contacts:
                print(contact.firstName, contact.lastName, contact.numbers)
    
    def ShowContacts(self):
        for contact in self.contacts:
            print(contact.firstName, contact.lastName, contact.numbers)
    
    def SearchForContactName(self, firstName, lastName):
        for contact in self.contacts:
            if contact.firstName == firstName and contact.lastName == lastName:
                print(contact.firstName, contact.lastName, contact.numbers)
    
    def SearchForContactNumber(self, number):
        for contact in self.contacts:
            if number in contact.numbers:
                print(contact.firstName, contact.lastName, contact.numbers)

    def SortContactsByFirstName(self):
        def GetFirstName(contact):
            return contact.firstName
        self.contacts.sort(key=GetFirstName)                
    
    def SortContactsByLastName(self):
        self.contacts.sort(key=lambda contact: contact.lastName)   

class Contact():
    def __init__(self, firstName, lastName, numbers):
        self.firstName = firstName
        self.lastName = lastName
        self.numbers = list(numbers)
            

if __name__ == "__main__":
    phone = Phone()
    phone.AddContact("Radek", "Szczygielski", "668107042")
    phone.AddContact("Marek", "Kowalski", "123456789", "257326791", "123456781")
    phone.AddContact("Marek", "Kowalski", "12345678910")
    phone.SaveFile()
    phone.ReadContacts()
    # phone.SortContactsByFirstName()
    # phone.ShowContacts()
    # phone.SortContactsByLastName()
    # phone.ShowContacts()


    # phone.SearchForContactName("Radek", "Szczygielski")
    # phone.ReadContacts()



#osobna metoda na zapisywanie do pliku oraz usunięnie zapisaywania w addcontact DONE
# w addcontacnt dodaje tylko po innym numerze jak istnieje to nie dodaje DONE
#sprawadznie czy numer jest odpowiednio długi, DONE
# wyszykujesz kontakty(metoda), DONE
# szukanie numeru telefony(metoda), DONE
# sortowanie po imieniu lub nazwisku DONE
# dodawanie numerów do jednej osoby, DONE
# dodać linijkę w której jest błąd info warrning do logger 
#save ma sprawdzać czy kontakt jest w pliku jak jest to nie zapisuje
#lista numerów to numery mają mieć sówj typ, pierwszy numer to np work, fax, personal, mobile, home 