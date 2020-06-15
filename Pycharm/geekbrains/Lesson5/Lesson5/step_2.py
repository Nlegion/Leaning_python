my_fyle_1 = open('docs/text_1.txt', 'r', encoding='utf-8')

# file_content = my_fyle_1.read().splitlines()
# file_content = my_fyle_1.readlines()
file_content = list(map(str.strip, my_fyle_1.readlines()))
print(file_content)

my_fyle_1.close()
