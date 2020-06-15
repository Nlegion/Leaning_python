with open('docs/text_2.txt', 'r+', encoding='utf-8') as my_fyle_1:
    my_fyle_1.seek(64)
    my_fyle_1.writelines([
        '|Продолжаем работу|\n',
        '|Запись файлов изучаем|\n'
    ])
