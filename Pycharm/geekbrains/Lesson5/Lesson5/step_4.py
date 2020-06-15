my_fyle_1 = open('docs/text_1.txt', encoding='utf-8')

file_content = my_fyle_1.read(14)  # binary data -> chunk = 1024
print(file_content)
file_content = my_fyle_1.read(14)  # binary data
print(file_content)
file_content = my_fyle_1.read(14)  # binary data
print(file_content)


my_fyle_1.close()
