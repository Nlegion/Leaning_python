with open('docs/text_2.txt', 'r', encoding='utf-8') as my_fyle_1:
    # for line in my_fyle_1.readlines():
    while True:
        # line = my_fyle_1.read(10)
        line = my_fyle_1.readline()
        if not line:
            break
        print(my_fyle_1.tell(), line)
