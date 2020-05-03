import os

def create_folders ():
   for i in range (1,100):
       folder_name = f'dir{i}'
       os.mkdir(folder_name)

def delete_folders ():
       for i in range (1,100):
           folder_name = f'dir{i}'
           os.rmdir(folder_name)

create_folders()
delete_folders()
