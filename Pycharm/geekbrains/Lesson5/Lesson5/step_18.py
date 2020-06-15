import os

file_name = 'step_1.py'
full_abs_path = os.path.abspath(file_name)
print(full_abs_path)

dir_name, file_name = os.path.split(full_abs_path)
print(os.path.split(full_abs_path)[0])
print(os.path.split(full_abs_path)[1])
print(os.path.split(full_abs_path))
print(dir_name, file_name)
