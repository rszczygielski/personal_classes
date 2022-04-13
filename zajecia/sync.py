import os
import shutil
import argparse

from numpy import source
# shutil.rmtree - usuwanie 


def get_catalogs_and_files(path: str, all_files: list):
    catalogs_and_files = os.listdir(path)
    for elem in catalogs_and_files:
        all_files.append(os.path.join(path, elem))
        if os.path.isdir(os.path.join(path, elem)):
            get_catalogs_and_files(os.path.join(path, elem), all_files)


def copy_to_destination(source: str, destination: str):
    all_files = []
    get_catalogs_and_files(source, all_files)
    for file in all_files:
        extra_catalog = file.replace(source, "")
        destination_file_or_catalog = '%s\%s'%(destination, extra_catalog)
        if os.path.isdir(file):
            if not os.path.isdir(destination_file_or_catalog):
                os.mkdir(destination_file_or_catalog)
        else:
            if not os.path.isfile(destination_file_or_catalog):
                shutil.copy(file, destination_file_or_catalog)

def delete_from_destination(source_path, destination_path):
    destination_files_paths = []
    source_files_paths = []
    get_catalogs_and_files(destination_path, destination_files_paths)
    get_catalogs_and_files(source_path, source_files_paths)
    source_files = []
    for file in source_files_paths:
        source_files.append(file.replace(source_path, ""))
    for file in destination_files_paths:
        extra_catalog_or_file = file.replace(destination_path, "")
        if extra_catalog_or_file not in source_files:
            if os.path.isfile(file):
                os.remove(file)
                # Changed in version 3.8: On Windows, will no longer delete the contents of a directory junction before removing the junction.
                # os.removedirs(file)
            else:
                # shutil.rmtree(file, ignore_errors=True)
                # os.removedirs(file)
                shutil.rmtree(file, ignore_errors=True)  #nie działa usuwa tylko katalogi, ale to chyba wina windowsa
                
    

def run(source_path, destination_path):
    number = input("""
        Press 1 to copy all files to directory
        Press 2 delete all files diffrent from the source: """)
    if number == "1":
        copy_to_destination(source_path, destination_path)
    elif number == "2":
        delete_from_destination(source_path, destination_path)
    else:
        print("Please input correct data")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='program which can copy or delete files and catalogs which are in destination and dont in source')
    parser.add_argument('src', metavar='source', type=str,
                    help='source catalog')
    parser.add_argument('des', metavar='destinatin', type=str,
                    help='destination catalog')
    parser.add_argument('-d', "--syc-delete", action="store_true", default=False, dest="sync_delete", required=False,
                    help='delete files and catalogs which are in destination and dont in source')
    arg = parser.parse_args()

    source_dir = arg.src
    destination_dir = arg.des
    issync_delete = arg.sync_delete

    copy_to_destination(source_dir, destination_dir)
    if issync_delete:
        delete_from_destination(source_dir, destination_dir)
    # sync(r"C:\Users\radek\Desktop\Python VSD\test1", r"C:\Users\radek\Desktop\Python VSD\test2")
    # print("%sdfafdasfa%s"%(zmienna,zmienna))
    # delete_from_destination(r"C:\Users\radek\Desktop\Python VSD\test1", r"C:\Users\radek\Desktop\Python VSD\test2")
    # run(r"C:\Users\radek\Desktop\Python VSD\zajecia\test1", r"C:\Users\radek\Desktop\Python VSD\zajecia\test2")
    