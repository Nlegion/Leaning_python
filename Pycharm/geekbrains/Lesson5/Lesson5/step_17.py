import os

for root, dirs, files in os.walk('.'):
    for file in files:
        # full_path = f'{root}/{file}'
        full_path = os.path.join(root, file)
        print(full_path, os.path.abspath(full_path))
