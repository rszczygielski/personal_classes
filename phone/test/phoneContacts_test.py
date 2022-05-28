import unittest
import sys
import os
from unittest import TestCase
sys.path.insert(0,"/home/radeksz/Documents/python_VSC/personal_classes/phone/phone")
from phone import Phone
from phone import Number
from phone import NumberType

class PhoneContactsTest(TestCase):

    def testPhoneContacts(self):
        phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt")
        self.assertEqual(len(phone.contacts), 0)

    def testAddContact(self):
        phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt")
        lenContacts = len(phone.contacts)
        phone.addContact("name","lastName", Number("123457779", NumberType.HOME), Number("123456788", NumberType.MOBILE))
        self.assertEqual(len(phone.contacts), lenContacts+1)
    
    def testAddContactWithWrongNumber(self):
        phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt")
        lenContacts = len(phone.contacts)
        phone.addContact("name","lastName", Number("123456789", NumberType.HOME), Number("12345678910", NumberType.MOBILE))
        self.assertEqual(len(phone.contacts), lenContacts)
    
    def testIfContactFileIsNotExsist(self):
        phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt")
        self.assertFalse(os.path.isfile(phone.contactFile))
        phone.saveFile()
        self.assertTrue(os.path.isfile(phone.contactFile))
        os.remove(phone.contactFile)
    
    def testAddContactWithTheSameNumber(self):
        phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt")
        phone.addContact("name","lastName", Number("123457779", NumberType.HOME), Number("123456788", NumberType.MOBILE))
        lenContacts = len(phone.contacts)
        phone.addContact("name2","lastName2", Number("123457779", NumberType.HOME), Number("222222222", NumberType.MOBILE))
        self.assertEqual(len(phone.contacts), lenContacts)
    
    def testAddOnlyNumberToContact(self):
        phone = Phone("/home/radeksz/Documents/python_VSC/personal_classes/phone/phone/contactsTest.txt")
        phone.addContact("Krystian", "Rybka", Number("890459632", NumberType.PERSONAL))
        contactNumbers = len(phone.getContactNumbers("Krystian", "Rybka"))
        self.assertEqual(contactNumbers, 1)
        phone.addNumberToContact("Krystian", "Rybka", [Number("777777777", NumberType.PERSONAL)])
        newNumberList = phone.getContactNumbers("Krystian", "Rybka")
        self.assertEqual(contactNumbers+1, len(newNumberList))
    
    def testAddContactWithMail(self):
        phone = Phone()
        phone.addContact("Krystian", "Rybka", Number("890459632", NumberType.PERSONAL), Email("test_mail@gmail.com", EmailType.PERSONAL))
        
        
        
if __name__ == "__main__":
    unittest.main()
    # dorobić testy