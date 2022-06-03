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
            #newNumbersOrEmail = list of numbers structs or email structs
            if isinstance(newNumberOrEmail, Number):
                newNumberStruct = newNumberOrEmail
                # change name of a varibale
                if len(newNumberStruct.number) != 9:
                    Logger.WARNING("It is not a correct number")
                    return
                for contact in self.contacts:
                    # Loop through alredy exsiteng contacts
                    for numberStruct in contact.numbers:
                        # already exsisting in contacts numberStruct
                        if newNumberStruct.number == numberStruct.number:
                            Logger.WARNING("This number already exists")
                            return
                numbersStructList.append(newNumberStruct)
            if isinstance(newNumberOrEmail, Email):
                newEmailStruct = newNumberOrEmail
                if not "@" in newEmailStruct.email:
                    Logger.WARNING("E-mail is not correct")
                    return
                for contact in self.contacts:
                    # Loop through alredy exsiteng contacts
                    for emailStruct in contact.emails:
                        # already exsisting in contacts emailStruct 
                        if newEmailStruct.email == emailStruct.email:
                            Logger.WARNING("This email already exists")
                            return
                eMailsStructList.append(newEmailStruct)
        self.contacts.append(Contact(firstName, lastName,numbersStructList, eMailsStructList))

    def saveFile(self):
        contactFile = open(self.contactFile, "w")
        for contact in self.contacts:
            numbersString = ""
            emailsString = ""
            if len(contact.numbers) != 0:
                # check if there is number to add
                for number in contact.numbers[:-1]:
                    numType = number.numberType.name
                    numbersString += f"{numType}:{number.number}" + " "
                    # createing a string of numbers to save from first to last but one
                lastNumberStruct = contact.numbers[-1]
                numbersString += f"{lastNumberStruct.numberType.name}:{lastNumberStruct.number}"
                # adding a last number to string to save
            if len(contact.emails) != 0:
                # check if there is email to add
                for email in contact.emails[:-1]:
                    emailType = email.emailType.name
                    emailsString += f"{emailType}:{email.email}" + " "
                    # createing a string of emails to save from first to last but one
                lastEmailStruct = contact.emails[-1]
                emailsString += f"{lastEmailStruct.emailType.name}:{lastEmailStruct.email}"
                # adding a last email to string to save
            contactLine = f"{contact.firstName} {contact.lastName} {numbersString} {emailsString}"
            # linking all strings together to save
            contactFile.write(contactLine)
            contactFile.write("\n")
        contactFile.close()

    def readContacts(self):
        if not os.path.isfile(self.contactFile):
            Logger.WARNING("There is no such file as contacts.txt")
            return  
            # w przypadku małego projektu można użyć tak return ale na większą skale może być problem bo ciężko 
            # znaleźć taki błąd i debugować to, ale tutaj dodatkowo mamy loga z errorem
        lines = open(self.contactFile).readlines()
        if len(lines) == 0:
            Logger.WARNING("There is no contacts in file")
        else:
            for line in lines:
                line = line.strip()
                splitedLine = line.split()
                firstName = splitedLine[0]
                lastName = splitedLine[1]
                numbersAndEmails = splitedLine[2:]
                # spliting all emails and numbers to one list
                numberStructList = []
                emailStructList = []
                for numberOrEmail in numbersAndEmails:
                    if "@" in numberOrEmail:
                        # all emails have @ so if @ in numberOrEmail program knows that it is an email
                        splitedEmail = numberOrEmail.split(":")
                        emailType = splitedEmail[0]
                        email = splitedEmail[1]
                        newEmail = Email(email, EmailType(emailType))
                        # creating a new structure of email
                        emailStructList.append(newEmail)
                        # adding an email struct to list of email structs
                    else:
                        # if @ not in numberOrEmail program knows that it is a number
                        splitedNumber = numberOrEmail.split(":")
                        numberType = splitedNumber[0]
                        number = splitedNumber[1]
                        newNumber = Number(number, NumberType(numberType))
                        # creating a new structure of number
                        numberStructList.append(newNumber)
                        # adding an number struct to list of number structs
                self.contacts.append(Contact(firstName, lastName, numberStructList, emailStructList))
            
    def showContacts(self):
        for contact in self.contacts:
            numbersToPrintList = []
            emailsToPrintList = []
            for numberStruct in contact.numbers:
                numberToPrint = f"{numberStruct.numberType.name}: {numberStruct.number}"
                numbersToPrintList.append(numberToPrint)
                # adding number sctructs to list 
            for emailStruct in contact.emails:
                emailToPrint = f"{emailStruct.emailType.name}: {emailStruct.email}"
                emailsToPrintList.append(emailToPrint)
                # adding email sctructs to list
            contactToPrint = f"{contact.firstName} {contact.lastName}" 
            if len(emailsToPrintList) != 0 :
                contactToPrint += f" {str(emailsToPrintList)}"
            if len(numbersToPrintList) != 0:
                contactToPrint += f" {str(numbersToPrintList)}"
            print(contactToPrint)
                
    
    def addNumberToContact(self, firstName, lastName, numberStructList:list):
        for contact in self.contacts:
            if contact.firstName == firstName and contact.lastName == lastName:
                for numberStruct in numberStructList:
                    contact.numbers.append(numberStruct)
    
    def addEmailToContact(self, firstName, lastName, emailStructList:list):
        for contact in self.contacts:
            if contact.firstName == firstName and contact.lastName == lastName:
                for emailStruct in emailStructList:
                    contact.emails.append(emailStruct)
    
    def getContactNumbers(self, firstName, lastName):
        for contact in self.contacts:
            if contact.firstName == firstName and contact.lastName == lastName:
                return contact.numbers
    
    def getContactEmails(self, firstName, lastName):
        for contact in self.contacts:
            if contact.firstName == firstName and contact.lastName == lastName:
                return contact.emails
               
    def searchForContactNumber(self, number):
        for contact in self.contacts:
            for numberStruct in contact.numbers:
                if number in numberStruct.number:
                    print(contact.firstName, contact.lastName, numberStruct.number, numberStruct.numberType.name)

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
    def __init__(self, email, emailType:EmailType):
        self.email = email
        self.emailType = emailType

class Number():
    def __init__(self, number:str, numberType:NumberType):
        self.number = number
        self.numberType = numberType 
            

if __name__ == "__main__":
    phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contacts.txt")
    phone.addContact("Radek", "Szczygielski", Number("668107042", NumberType.PERSONAL))
    phone.addContact("Marek", "Kowalski", Number("123456789", NumberType.HOME), Number("257326791", NumberType.FAX), Number("123456781", NumberType.WORK))
    phone.addContact("Marek", "Kowalski", Number("12345678910", NumberType.MOBILE))
    phone.addContact("Krystian", "Rybka", Number("890459632", NumberType.PERSONAL),)
    phone.addContact("Radek2", "Szczygielski2", Number("888888888", NumberType.PERSONAL), Email("testmail@test.com", EmailType.PERSONAL))
    # phone.addNumberToContact("Radek", "Szczygielski", [Number("111111111", NumberType.FAX)])
    phone.showContacts()
    print(30 * "-")
    phone.getContactNumbers("Radek2", "Szczygielski2")
    phone.getContactEmails("Radek2", "Szczygielski2")
    phone.searchForContactNumber("668107042")
    print(30 * "-")
    phone.sortContactsByFirstName()
    phone.showContacts()
    print(30 * "-")
    phone.addNumberToContact("Radek", "Szczygielski", [Number("777777777", NumberType.PERSONAL)])
    print(phone.getContactNumbers("Radek", "Szczygielski"))

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
# zwróc wszystkie kontakty które mają to samo imię lub nazwisko
# smtp lib ogarnij i zrób mail