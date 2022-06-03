from shutil import which
import unittest
import sys
import os
from unittest import TestCase
sys.path.insert(0,"/home/radeksz/Documents/python_VSC/personal_classes/phone/phone")
from phone import Phone
from phone import Number
from phone import NumberType
from phone import Email
from phone import EmailType

class PhoneContactsTest(TestCase):

    def testPhoneContacts(self):
        phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt")
        self.assertEqual(len(phone.contacts), 0)

    def testAddContact(self):
        phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt")
        lenContacts = len(phone.contacts)
        phone.addContact("firstName","lastName", Number("123457779", NumberType.HOME), Number("123456788", NumberType.MOBILE))
        self.assertEqual(len(phone.contacts), lenContacts+1)
    
    def testAddContactWithWrongNumber(self):
        phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt")
        lenContacts = len(phone.contacts)
        phone.addContact("firstName","lastName", Number("123456789", NumberType.HOME), Number("12345678910", NumberType.MOBILE))
        self.assertEqual(len(phone.contacts), lenContacts)
    
    def testIfContactFileIsNotExsist(self):
        phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt")
        self.assertFalse(os.path.isfile(phone.contactFile))
        phone.saveFile()
        self.assertTrue(os.path.isfile(phone.contactFile))
        os.remove(phone.contactFile)
    
    def testAddContactWithTheSameNumber(self):
        phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt")
        phone.addContact("firstName","lastName", Number("123457779", NumberType.HOME), Number("123456788", NumberType.MOBILE))
        lenContacts = len(phone.contacts)
        phone.addContact("firstName2","lastName2", Number("123457779", NumberType.HOME), Number("222222222", NumberType.MOBILE))
        self.assertEqual(len(phone.contacts), lenContacts)
    
    def testAddOnlyNumberToContact(self):
        phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt")
        phone.addContact("firstName", "lastName", Number("890459632", NumberType.PERSONAL))
        contactNumbers = len(phone.getContactNumbers("firstName", "lastName"))
        self.assertEqual(contactNumbers, 1)
        phone.addNumberToContact("firstName", "lastName", [Number("777777777", NumberType.PERSONAL)])
        newNumberList = phone.getContactNumbers("firstName", "lastName")
        self.assertEqual(contactNumbers+1, len(newNumberList))
    
    def testAddOnlyEmailToContact(self):
        phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt")
        phone.addContact("firstName", "lastName", Email("test_mail@gmail.com", EmailType.PERSONAL))
        contactEmails = len(phone.getContactEmails("firstName", "lastName"))
        self.assertEqual(contactEmails, 1)
        phone.addEmailToContact("firstName", "lastName", [Email("test_mail2@gmail.com", EmailType.PERSONAL)])
        newEmailList = phone.getContactEmails("firstName", "lastName")
        self.assertEqual(contactEmails+1, len(newEmailList))
    
    def testAddContactWithMail(self):
        phone = Phone('/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt')
        lenContacts = len(phone.contacts)
        phone.addContact("firstName", "lastName", Number("890459632", NumberType.PERSONAL), Email("test_mail@gmail.com", EmailType.PERSONAL))
        self.assertEqual(len(phone.contacts), lenContacts+1)
    
    def testAddContactWithTheSameMail(self):
        phone = Phone('/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt')
        phone.addContact("firstName", "lastName", Number("890459632", NumberType.PERSONAL), Email("test_mail@gmail.com", EmailType.PERSONAL))
        lenContacts = len(phone.contacts)
        phone.addContact("firstName2", "lastname2", Number("777777777", NumberType.PERSONAL), Email("test_mail@gmail.com", EmailType.WORK))
        self.assertEqual(len(phone.contacts), lenContacts)
    
    def testSaveToFile(self):
        phone = Phone('/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt')
        phone.saveFile()
        with open(phone.contactFile) as contactFile:
            zeroLines = len(contactFile.readlines())
        self.assertEqual(zeroLines, 0)
        phone.addContact("firstName", "lastName", Number("890459632", NumberType.PERSONAL), Email("test_mail@gmail.com", EmailType.PERSONAL))
        phone.saveFile()
        with open(phone.contactFile) as contactFile:
            newLineFileLen = len(contactFile.readlines())
        self.assertEqual(newLineFileLen, 1)
        self.assertNotEqual(zeroLines, newLineFileLen)
        self.assertEqual(zeroLines+1, newLineFileLen)
        os.remove(phone.contactFile)
    
    def testReadContacts(self):
        phone = Phone('/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt')
        phone.saveFile()
        phone.readContacts()
        zeroContacts = len(phone.contacts)
        self.assertEqual(zeroContacts, 0)
        with open(phone.contactFile, "w") as contactFile:
            contactFile.write("firstName lastName PERSONAL:888888888 PERSONAL:testmail@test.com ")
        phone.readContacts()
        newContactLen = len(phone.contacts)
        self.assertEqual(newContactLen, 1)
        self.assertNotEqual(zeroContacts, newContactLen)
        self.assertEqual(zeroContacts+1, newContactLen)
        os.remove(phone.contactFile)
        
if __name__ == "__main__":
    unittest.main()
    # dorobić testy