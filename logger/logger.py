from datetime import datetime
from inspect import stack

class Logger():
    def __init__(self):
        self.date_bool = True
        self.log_level_bool = True
    
    def settings(self, showLog_level=True, show_date=True):
        if show_date:
            self.date_bool = True
        else:
            self.date_bool = False
        if showLog_level:
            self.log_level_bool = True
        else:
            self.log_level_bool = False

    def time(self):
        return datetime.now().strftime("%Y %m %d %H:%M:%S")
        
    def file_name(self):
        return stack()[2].filename.split("/")[-1]

    def arguments(self, arguments):
        printer = ""
        for elem in arguments:
            printer += " " + elem
        return printer
    
    def INFO(self, *argument):
        whole_communique_list = [self.time(), self.file_name(), "INFO:", self.arguments(argument)]
        if self.date_bool and self.log_level_bool:
            print(" ".join(whole_communique_list))
        elif self.date_bool == False and self.log_level_bool:
            print(" ".join(whole_communique_list[1:]))
        elif self.date_bool and self.log_level_bool == False:
            print(" ".join(whole_communique_list[:2])+ " ".join(whole_communique_list[3:]))
        else:
            print(whole_communique_list[1] + whole_communique_list[-1])
        
    def WARNING(self, *argument):
        whole_communique_list = [self.time(), self.file_name(), "WARNING:", self.arguments(argument)]
        if self.date_bool and self.log_level_bool:
            print("\033[93m" + " ".join(whole_communique_list), "\033[0m")
        elif self.date_bool == False and self.log_level_bool:
            print("\033[93m" + " ".join(whole_communique_list[1:]),"\033[0m")
        elif self.date_bool and self.log_level_bool == False:
            print("\033[93m" + " ".join(whole_communique_list[:2])+ " ".join(whole_communique_list[3:]),"\033[0m")
        else:
            print("\033[93m" + whole_communique_list[1] + whole_communique_list[-1],"\033[0m")
    
    def ERROR(self, *argument):
        whole_communique_list = [self.time(), self.file_name(), "ERROR:", self.arguments(argument)]
        if self.date_bool and self.log_level_bool:
            print("\033[91m" + " ".join(whole_communique_list), "\033[0m")
        elif self.date_bool == False and self.log_level_bool:
            print("\033[91m" + " ".join(whole_communique_list[1:]), "\033[0m")
        elif self.date_bool and self.log_level_bool == False:
            print("\033[91m" + " ".join(whole_communique_list[:2])+ " ".join(whole_communique_list[3:]), "\033[0m")
        else:
            print("\033[91m" + whole_communique_list[1] + whole_communique_list[-1], "\033[0m")

#ustawienia - na przykład tylko error printuje, zapis logeru do pliku(określonego), samemmu sobie ustawić czy ma pokazywać date albo w ogóle wyłączay napis ERORR albo INFO 
    
    

    
    





