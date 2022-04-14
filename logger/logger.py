from datetime import datetime
from inspect import stack
class Logger():
    
    def settings(self, showLog_level=True, show_date=True):
        pass 


    def time(self):
        return datetime.now().strftime("%Y %m %d %H:%M:%S")
    def file_name(self):
        return stack()[2].filename.split("\\")[-1]
    def arguments(self, arguments):
        printer = ""
        for elem in arguments:
            printer += " " + elem
        return printer
    
    def INFO(self, *argument):
        strin = self.time() + self.file_name() + "INFO:" + self.arguments(argument)
        print(self.time(), self.file_name(), "INFO:", self.arguments(argument))
        print(strin)

    def WARNING(self, *argument):
        print("\033[93m" + self.time(), self.file_name(), "WARNING:", self.arguments(argument),"\033[0m")
    
    def ERROR(self, *argument):
        print("\033[91m" + self.time(), self.file_name(), "ERROR:", self.arguments(argument), "\033[0m")

#ustawienia - na przykład tylko error printuje, zapis logeru do pliku(określonego), samemmu sobie ustawić czy ma pokazywać date albo w ogóle wyłączay napis ERORR albo INFO 
    
    

    
    





