# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func_ascii(z):
    return chr(int(ord(z)) - 32)


def int_func_title(z):
    return z.title()


def int_func_voc(z):
    voc = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F',
           'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L',
           'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S',
           't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
    return voc.get(z)


def breaking_word(com_word):
    a = com_word[:1]
    b = com_word[1:]
    a = int_func_ascii(a)
    return a + b


word = 'word'
a = word[:1]
b = word[1:]

print('Слово функцией title: {0}'.format(int_func_title(word)))
print('Слово функцией ascii: {0}{1}'.format(int_func_ascii(a), b))
print('Слово функцией voc: {0}{1}'.format(int_func_voc(a), b))

sentence = 'quod licet iovi non licet bovi '
seq_sent = sentence.split()
idx = 0

while idx < len(seq_sent):
    seq_sent[idx] = breaking_word(seq_sent[idx])
    idx += 1
print('Текст: {0}'.format(' '.join(seq_sent)))
