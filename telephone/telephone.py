import random

class Phone():
    def __init__(self, money = 10):
        self.money = money

    "przykład zmiennej statycznej, zmieniamy ją poprzez Phone.zmienna_statyczna"
    call_price_per_minute = 0.4
    sms_price = 0.05

    def calling(self):
        print("Calling...")
        calling_time = random.randint(1, 60) #przykład funkcji statycznej, bo od razu podaje się zmienną bez odwoływania się do metody(funkcji w klasie)
        price_for_call = calling_time * Phone.call_price_per_minute
        print(f"Price for call: {price_for_call}")
        print(Phone.call_price_per_minute)
        self.money -= price_for_call
    
    def sms(self):
        print("Texting...")
        self.money -= Phone.sms_price

    def money_check(self):
        # print(f"There is {self.money} on your account")
        print("There is %s on your account"%(self.money))
    

if __name__ == "__main__":
    phones = {"phone1": Phone(20), "phone2": Phone(), "phone3": Phone(5)}
    
    print("Phone 1", "-" * 30)
    phones["phone1"].calling()
    phones["phone1"].sms()
    print("Phone 2", "-" * 30)
    phones["phone2"].calling()
    phones["phone2"].sms()
    print("Phone 3", "-" * 30)
    phones["phone3"].calling()
    phones["phone3"].sms()
    for phone in phones.values():
        phone.money_check()
    

    Phone.call_price_per_minute = 1
    Phone.sms_price = 0.4


    print("Phone 1", "-" * 30)
    phones["phone1"].calling()
    phones["phone1"].sms()
    print("Phone 2", "-" * 30)
    phones["phone2"].calling()
    phones["phone2"].sms()
    print("Phone 3", "-" * 30)
    phones["phone3"].calling()
    phones["phone3"].sms()
    for phone in phones.values():
        phone.money_check()
    


    