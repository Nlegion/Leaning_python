my_fyle_1 = open('docs/text_1.txt', 'r', encoding='utf-8')
# print(type(my_fyle_1))
# print(dir(my_fyle_1))

file_content = my_fyle_1.read()
print(file_content)

my_fyle_1.close()
