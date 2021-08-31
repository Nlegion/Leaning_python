# Дополнить следующую функцию недостающим кодом:
# Функция принимает имя каталога и распечатывает его содержимое
# в виде «путь и имя файла», а также любые другие
# файлы во вложенных каталогах.
import os


def print_directory_contents(sPath):
    struct = []
    for file_or_directory in os.listdir(sPath):
        full_name = os.path.join(os.path.abspath(sPath), file_or_directory)
        if os.path.isfile(full_name):
            struct.append((os.path.abspath(sPath), file_or_directory))
        else:
            struct.extend(print_directory_contents(full_name))
    return struct


print(print_directory_contents('/var/log'))
