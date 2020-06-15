with open('docs/text_2.txt', 'w', encoding='utf-8') as my_fyle_1:
    my_fyle_1.write('Продолжаем работу.\n')
    my_fyle_1.write('Запись файлов изучаем.\n')

# for el in range(5):
#     with open('docs/text_2.txt', 'r', encoding='utf-8') as my_fyle_1:
#         file_content = my_fyle_1.read().splitlines()
#         print(file_content)

with open('docs/text_2.txt', 'r', encoding='utf-8') as my_fyle_1:
    file_content = my_fyle_1.read().splitlines()

print(file_content)
