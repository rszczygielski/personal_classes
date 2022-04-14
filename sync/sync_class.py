import os
import shutil
import argparse

class Sync():
    def __init__(self, source: str, destination:str):
        self.source = source
        self.destination = destination
        

    def get_catalogs_and_files(self, path: str, all_files: list):
        catalogs_and_files = os.listdir(path)
        for elem in catalogs_and_files:
            all_files.append(os.path.join(path, elem))
            if os.path.isdir(os.path.join(path, elem)):
                self.get_catalogs_and_files(os.path.join(path, elem), all_files)


    def copy_to_destination(self):
        all_files = []
        self.get_catalogs_and_files(self.source, all_files)
        for file in all_files:
            extra_catalog = file.replace(self.source, "")
            destination_file_or_catalog = '%s\%s'%(self.destination, extra_catalog)
            if os.path.isdir(file):
                if not os.path.isdir(destination_file_or_catalog):
                    os.mkdir(destination_file_or_catalog)
            else:
                if not os.path.isfile(destination_file_or_catalog):
                    shutil.copy(file, destination_file_or_catalog)

    def delete_from_destination(self):
        destination_files_paths = []
        source_files_paths = []
        self.get_catalogs_and_files(self.destination, destination_files_paths)
        self.get_catalogs_and_files(self.source, source_files_paths)
        source_files = []
        for file in source_files_paths:
            source_files.append(file.replace(self.source, ""))
        for file in destination_files_paths:
            extra_catalog_or_file = file.replace(self.destination, "")
            if extra_catalog_or_file not in source_files:
                if os.path.isfile(file):
                    os.remove(file) 
                else:
                    shutil.rmtree(file, ignore_errors=True)  #nie działa usuwa tylko katalogi, ale to chyba wina windowsa
                
    

def run(source_path, destination_path):
    sync = Sync(source_path, destination_path)
    number = input("""
        Press 1 to copy all files to directory
        Press 2 delete all files diffrent from the source: """)
    if number == "1":
        sync.copy_to_destination()
    elif number == "2":
        sync.delete_from_destination()
    else:
        print("Please input correct data")


if __name__ == "__main__":
    
    # sync(r"C:\Users\radek\Desktop\Python VSD\test1", r"C:\Users\radek\Desktop\Python VSD\test2")
    # print("%sdfafdasfa%s"%(zmienna,zmienna))
    # delete_from_destination(r"C:\Users\radek\Desktop\Python VSD\test1", r"C:\Users\radek\Desktop\Python VSD\test2")
    run(r"C:\Users\radek\Desktop\Python VSD\zajecia\test1", r"C:\Users\radek\Desktop\Python VSD\zajecia\test2")