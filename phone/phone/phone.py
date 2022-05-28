import email
import sys
sys.path.insert(0,"/home/radeksz/Documents/python_VSC/personal_classes/phone/logger")
from logger import Logger
from enum import Enum
import os
# przez to, że w programie logger.py stworzyłem instancje LoggerClass to nie muszę tworzyć podaczas inportu 
# testy jednostkowe i intregracyjne, jednoskowe to takie które kod testuje sam siebie, a integracujne to są takie które są napisane w innym programie


class NumberType(Enum):
        WORK = "WORK"
        FAX = "FAX"
        PERSONAL = "PERSONAL"
        MOBILE = "MOBILE"
        HOME = "HOME"

class EmailType(Enum):
    WORK = "WORK"
    PERSONAL = "PERSONAL"
    UNIVERISTY = "UNIVERSITY"


class Phone():
    def __init__(self, contactFile:str):
        self.contacts = []
        self.contactFile = contactFile
        self.readContacts()

    
    def addContact(self, firstName:str, lastName:str, *newNumbersOrEmails):
        numbersStructList = []
        eMailsStructList = []
        for contact in self.contacts:
            if contact.firstName == firstName and contact.lastName == lastName:
                Logger.WARNING("Contact already exsists")
                return
        for newNumberOrEmail in newNumbersOrEmails:
            #newNUmbers = list of sutruct numbers
            if isinstance(newNumberOrEmail, Number):
                newNumberStruct = newNumberOrEmail
                if len(newNumberStruct.number) != 9:
                    Logger.WARNING("It is not a correct number")
                    return
                for contact in self.contacts:
                    # Loop through alredy exsiteng contacts
                    for numberStruct in contact.numbers:
                        # old number struct
                        if newNumberStruct.number == numberStruct.number:
                            Logger.WARNING("This numbers already exists")
                            return
                numbersStructList.append(newNumberStruct)
            elif isinstance(newNumberOrEmail, Email):
                newEmailStruct = newNumberOrEmail
                if not "@" in newEmailStruct.email:
                    Logger.WARNING("E-mail is not correct")
                    return
                for contact in self.contacts:
                    for emailStruct in contact.emails:
                        if newEmailStruct.email == emailStruct:
                            Logger.WARNING("This numbers already exists")
                            return
                eMailsStructList.append(newEmailStruct)
        self.contacts.append(Contact(firstName, lastName,numbersStructList, eMailsStructList))
    

    def addNumberToContact(self, firstName, lastName, numberStructList:list):
        for contact in self.contacts:
            if contact.firstName == firstName and contact.lastName == lastName:
                for numberStruct in numberStructList:
                    contact.numbers.append(numberStruct)

    
    def saveFile(self):
        contactFile = open(self.contactFile, "w")
        for contact in self.contacts:
            numbers = ""
            emails = ""
            countNumbers = len(contact.numbers)
            countEmails = len(contact.emails)
            if countNumbers != 0:
                for i in range(countNumbers):
                    numType = contact.numbers[i].numberType.name
                    if i != (countNumbers-1):
                        numbers += f"{numType}:{contact.numbers[i].number}" + " "
                    else:
                        numbers += f"{numType}:{contact.numbers[i].number}"
            if countEmails != 0:
                for i in range(countEmails):
                    emailType = contact.emails[i].emailType.name
                    if i != (countNumbers-1):
                        emails += f"{emailType}:{contact.email[i].email}" + " "
                    else:
                        emails += f"{emailType}:{contact.emails[i].email}"
            contactLine = f"{contact.firstName}  {contact.lastName}  {numbers}  {emails}"
            contactFile.write(contactLine)
            contactFile.write("\n")
        contactFile.close()

    def readContacts(self):
        if not os.path.isfile(self.contactFile):
            Logger.WARNING("There is no such file as contacts.txt")
            return  #w przypadku małego projekstu spoko ale na większa skale może być problem bo ciężko znaleźć taki błąd, ale tutaj dodatkowo mamy loga z errorem
        lines = open(self.contactFile).readlines()
        if len(lines) == 0:
            Logger.WARNING("There is no contacts in file")
        else:
            for line in lines:
                line = line.strip()
                splitedLine = line.split()
                firstName = splitedLine[0]
                lastName = splitedLine[1]
                numbersAndEmail = splitedLine[2:]
                numberStructList = []
                emailStructList = []
                for numberOrEmail in numbersAndEmail:
                    if "@" in numbersAndEmail:
                        splitedEmail = numberOrEmail.split(":")
                        emailType = splitedEmail[0]
                        email = splitedEmail[1]
                        newEmail = Email(email, emailType)
                        emailStructList.append(newEmail)
                    else:    
                        splitedNumber = numberOrEmail.split(":")
                        numberType = splitedNumber[0]
                        number = splitedNumber[1]
                        newNumber = Number(number, NumberType(numberType))
                        numberStructList.append(newNumber)
                self.contacts.append(Contact(firstName, lastName, numberStructList, emailStructList))
            
    def showContacts(self):
        for contact in self.contacts:
            numbersToPrint = []
            emailsToPrint = []
            for numberStruct in contact.numbers:
                numberToPrint = f"{numberStruct.numberType.name}: {numberStruct.number}"
                numbersToPrint.append(numberToPrint)
            for emailStruct in contact.emails:
                emailToPrint = f"{emailStruct.emailType.name}: {emailStruct.email}"
                emailsToPrint.append(emailToPrint)
            print(contact.firstName, contact.lastName, numbersToPrint, emailsToPrint)
    
    def getContactNumbers(self, firstName, lastName):
        for contact in self.contacts:
            if contact.firstName == firstName and contact.lastName == lastName:
                return contact.numbers
    
    def searchForContactNumber(self, number):
        for contact in self.contacts:
            if number in contact.numbers:
                print(contact.firstName, contact.lastName, contact.numbers)

    def sortContactsByFirstName(self):
        def GetFirstName(contact):
            return contact.firstName
        self.contacts.sort(key=GetFirstName)  

class Contact():
    def __init__(self, firstName, lastName, numbers, emails):
        self.firstName = firstName
        self.lastName = lastName
        self.numbers = list(numbers)
        self.emails = list(emails)

class Email():
    def __init__(self, email, emailType):
        self.email = email
        self.emailType = emailType

class Number():
    def __init__(self, number:str, numberType:NumberType):
        self.number = number
        self.numberType = numberType 
            

if __name__ == "__main__":
    phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contacts.txt")
    phone.addContact("Radek", "Szczygielski", Number("668107042", NumberType.PERSONAL))
    phone.addContact("Marek", "Kowalski", Number("123456789", NumberType.HOME),Number("257326791", NumberType.FAX),Number("123456781", NumberType.WORK))
    phone.addContact("Marek", "Kowalski", Number("12345678910", NumberType.MOBILE))
    phone.addContact("Krystian", "Rybka", Number("890459632", NumberType.PERSONAL),)
    phone.addContact("Radek2", "Szczygielski2", Number("888888888", NumberType.PERSONAL), Email("testmail@test.com", EmailType.PERSONAL))
    phone.showContacts()
    # phone.saveFile()

    # phone.SearchForContactName("Radek", "Szczygielski")
    # phone.ReadContacts()


# Radek2 Szczygielski2 PERSONAL:888888888 PERSONAL:testmail@test.com
#osobna metoda na zapisywanie do pliku oraz usunięnie zapisaywania w addcontact DONE
# w addcontacnt dodaje tylko po innym numerze jak istnieje to nie dodaje DONE
#sprawadznie czy numer jest odpowiednio długi, DONE
# wyszykujesz kontakty(metoda), DONE
# szukanie numeru telefony(metoda), DONE
# sortowanie po imieniu lub nazwisku DONE
# dodawanie numerów do jednej osoby, DONE
# dodać linijkę w której jest błąd info warrning do logger DONE
#save ma sprawdzać czy kontakt jest w pliku jak jest to nie zapisuje DONE
#lista numerów to numery mają mieć sówj typ, pierwszy numer to np work, fax, personal, mobile, home DONE
# read zrobić z Enumami DONE
# zrobić test na save file no ogólnie ile się da