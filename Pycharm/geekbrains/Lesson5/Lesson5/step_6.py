# with transaction.atomic():
#     data_1.save()
#     data_2.save()
#     data_3.save()
file_content = None
try:
    # num = float(input())
    with open('docs/text_2.txt', encoding='utf-8') as my_fyle_1:
        file_content = my_fyle_1.readline()
        print(file_content)
        file_content = my_fyle_1.readline()
        print(file_content)
        file_content = my_fyle_1.readline()
except FileNotFoundError as e:
    print(f'file not found: {e}')
except (FileExistsError, AttributeError, ValueError) as e:
    print(f'file exists: {e}')
except Exception as e:
    print(f'strange error: {e}')

print(file_content)
# 7 min -> 20:16 AIR

# __enter__()
# __exit__()
