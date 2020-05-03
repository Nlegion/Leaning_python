import sys
from core import create_folder, create_file, get_list, delete_file, copy_file, save_info,change_dir

save_info('старт')
try:
   command = sys.argv[1]
except IndexError:
   print('необходимо выбрать команду')
else:
   if command == 'list':
       get_list()
   elif command == 'create_file':
       try:
           name = sys.argv[2]
       except IndexError:
           print('нет названия файла')
       else:
           create_file(name)
   elif command == 'create_folder':
       try:
           name = sys.argv[2]
       except IndexError:
           print('нет названия папки')
       else:
           create_folder(name)
   elif command == 'delete':
       try:
           name = sys.argv[2]
       except IndexError:
           print('нет названия файла или папки')
       else:
           delete_file(name)
   elif command == 'change_dir':
       try:
           name = sys.argv[2]
       except IndexError:
           print('нет названия файла или папки')
       else:
           change_dir(name)
   elif command == 'copy':
       try:
           name = sys.argv[2]
           new_name = sys.argv[3]
       except IndexError:
           print('Необходимо название файла и назваине копии')
       else:
           copy_file(name,new_name)
   elif command == 'help':
       print('list - список файлов и папок')
       print('create_file - создание файла')
       print('create_folder - создание папки')
       print('delete - удаление файла или папки')
       print('copy - копирование файла или папки')

save_info('конец')
