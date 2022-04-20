from datetime import datetime
from inspect import stack
import os

class Logger():
    def __init__(self):
        self.settings()
    
    def settings(self, showLog_level=True, show_date=True, show_file_name=True, save_bool=False):
        self.date_bool = show_date
        self.log_level_bool = showLog_level
        self.file_name_bool = show_file_name
        self.save_bool = save_bool

    def time(self):
        return datetime.now().strftime("%Y %m %d %H:%M:%S")
        
    def file_name(self):
        return stack()[3].filename.split("/")[-1]

    def arguments(self, arguments):
        printer = ""
        for elem in arguments:
            printer += " " + elem
        return printer
    
    
    def get_log(self, log_level, argument):
        log = ""
        if self.date_bool:
            log += self.time() + " "
        if self.file_name_bool:
            log += self.file_name() + " "
        if self.log_level_bool:
            log += log_level + " "
        log += self.arguments(argument)
        return log
    
    def save_to_file(self):
        path = os.getcwd()
        if self.save_bool:
            name = input("Chose file name: ")
            open(path + "/" + name + ".txt", "w").write(self.info + "\n" + self.warning + "\n" + self.error)
        

    def INFO(self, *argument):
        print(self.get_log("INFO", argument))
        self.info = self.get_log("INFO", argument)
        
    def WARNING(self, *argument):
        print("\033[93m" + self.get_log("WARNING", argument),"\033[0m")
        self.warning = self.get_log("WARNING", argument)

    
    def ERROR(self, *argument):
        print("\033[91m" + self.get_log("ERROR", argument),"\033[0m")
        self.error = self.get_log("ERROR", argument)
    



#ustawienia, zapis logeru do pliku(określonego)
    
    

    
    





