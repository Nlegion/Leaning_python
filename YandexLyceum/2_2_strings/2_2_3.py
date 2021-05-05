word = input()
symb_n = int(input())
if symb_n > len(word) or symb_n < 1:
    print('ОШИБКА')
else:
    print(word[symb_n - 1])