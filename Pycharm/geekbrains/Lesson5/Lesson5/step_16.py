import os

my_file_items = os.listdir('.')
print(my_file_items)

my_files = [el for el in os.listdir('.') if os.path.isfile(el)]
# my_files = list(filter(os.path.isfile, os.listdir('.')))
print(my_files)

my_folders = [el for el in os.listdir('.') if os.path.isdir(el)]
print(my_folders)
