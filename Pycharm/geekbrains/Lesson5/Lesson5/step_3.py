my_fyle_1 = open('docs/text_1.txt', 'r', encoding='utf-8')

for line in my_fyle_1:  # as generator (slow)
    print(line, end='')
print()

my_fyle_1.close()
