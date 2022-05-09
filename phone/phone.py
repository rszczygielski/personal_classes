from itertools import count
from logger import Logger
from enum import Enum, auto
import os
# przez to, że w programie logger.py stworzyłem instancje LoggerClass to nie muszę tworzyć podaczas inportu 

class NumberType(Enum):
        WORK = auto()
        FAX = auto()
        PERSONAL = auto()
        MOBILE = auto()
        HOME = auto()

class Phone():
    def __init__(self):
        self.contacts = []
        self.nameFile = "contacts.txt"
        self.readContacts()

    
    def addContact(self, firstName:str, lastName:str, *numbers):
        for numberStruct in numbers:
            if len(numberStruct.number) != 9:
                Logger.WARNING("It is not a correct number")
                return
            for contact in self.contacts:
                if numberStruct.number in contact.numbers:
                    Logger.WARNING("This numbers already exists")
                    return                
        self.contacts.append(Contact(firstName, lastName, numbers))
        
    
    def saveFile(self):
        contactFile = open(self.nameFile)
        lineList = []
        for line in contactFile.readlines():
            lineList.append(line.strip())
        contactFile.close()
        contactFile = open(self.nameFile, "a")
        for contact in self.contacts:
            numbers = ""
            countNumbers = len(contact.numbers)
            for i in range(countNumbers):
                numType = contact.numbers[i].numberType.name
                if i != (countNumbers-1):
                    numbers += f"{numType}:{contact.numbers[i].number}" + " "
                else:
                    numbers += f"{numType}:{contact.numbers[i].number}"
            contactLine = contact.firstName + " " + contact.lastName + " "  + numbers
            if contactLine not in lineList:
                contactFile.write(contactLine)
                contactFile.write("\n")
        contactFile.close()
    
    
    def ifDuplicatesExsist(self, firstName:str, lastName:str, numbers):
        for contact in self.contacts:
            for numberStruct in contact.numbers:
                if contact.firstName == firstName and contact.lastName == lastName and numberStruct.number in numbers:
                    return True
        return False
    
    def checkNumberType(self, number, numberType):
        if numberType == NumberType.FAX.name:
            return Number(number, NumberType.FAX)
        if numberType == NumberType.HOME.name:
            return Number(number, NumberType.HOME)
        if numberType == NumberType.MOBILE.name:
            return Number(number, NumberType.MOBILE)
        if numberType == NumberType.PERSONAL.name:
            return Number(number, NumberType.PERSONAL)
        if numberType == NumberType.WORK.name:
            return Number(number, NumberType.WORK)
        

    def readContacts(self):
        if not os.path.isfile(self.nameFile):
            Logger.WARNING("There is no such file as contacts.txt")
            return  #w przypadku małego projekstu spoko ale na większa skale może być problem bo ciężko znaleźć taki błąd, ale tutaj dodatkowo mamy loga z errorem
        lines = open(self.nameFile).readlines()
        if len(lines) == 0:
            Logger.WARNING("There is no contacts in file")
        else:
            for line in lines:
                line = line.strip()
                splitedLine = line.split()
                if len(splitedLine) >= 3:
                    firstName = splitedLine[0]
                    lastName = splitedLine[1]
                    numbersInLine = splitedLine[2:]
                    numbers = []
                    for numberInLine in numbersInLine:
                        splitedNumber = numberInLine.split(":")
                        print(splitedNumber)
                        numberType = splitedNumber[0]
                        number = splitedNumber[1]
                        number = self.checkNumberType(number, numberType)
                        numbers.append(number)
                    self.contacts.append(Contact(firstName, lastName, numbers))
            for contact in self.contacts:
                numbersToPrint = []
                for numberStruct in contact.numbers:
                    numberToPrint = f"{numberStruct.numberType.name}: {numberStruct.number}"
                    numbersToPrint.append(numberToPrint)
                print(contact.firstName, contact.lastName, numbersToPrint)
    
    def showContacts(self):
        for contact in self.contacts:
            print(contact.firstName, contact.lastName, contact.numbers)
    
    def searchForContactName(self, firstName, lastName):
        for contact in self.contacts:
            if contact.firstName == firstName and contact.lastName == lastName:
                print(contact.firstName, contact.lastName, contact.numbers)
    
    def searchForContactNumber(self, number):
        for contact in self.contacts:
            if number in contact.numbers:
                print(contact.firstName, contact.lastName, contact.numbers)

    def sortContactsByFirstName(self):
        def GetFirstName(contact):
            return contact.firstName
        self.contacts.sort(key=GetFirstName)                
    
    def sortContactsByLastName(self):
        self.contacts.sort(key=lambda contact: contact.lastName)   

class Contact():
    def __init__(self, firstName, lastName, numbers):
        self.firstName = firstName
        self.lastName = lastName
        self.numbers = list(numbers)

class Number():
    def __init__(self, number:str, numberType:NumberType):
        self.number = number
        self.numberType = numberType 
            

if __name__ == "__main__":
    phone = Phone()
    phone.addContact("Radek", "Szczygielski", Number("668107042", NumberType.PERSONAL))
    phone.addContact("Marek", "Kowalski", Number("123456789", NumberType.HOME),Number("257326791", NumberType.FAX),Number("123456781", NumberType.WORK))
    phone.addContact("Marek", "Kowalski", Number("12345678910", NumberType.MOBILE))
    phone.saveFile()
    # phone.readContacts()
    # phone.sortContactsByFirstName()
    # phone.showContacts()
    # phone.sortContactsByLastName()
    # phone.showContacts()


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
# read zrobić z Enumami