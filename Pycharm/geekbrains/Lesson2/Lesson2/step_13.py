a = 'Привет '
b = 'меня '
c = 'зовут '
d = 'Иван '

# greeting = a
# greeting += b
# greeting += c
# greeting += d  # immutable
# print(greeting)
# print(a + b + c + d)
print(f'{a}{b}{c}{d}')  # good

greeting = []
greeting.append(a)
greeting.append(b)
greeting.append(c)
greeting.append(d)

print(''.join(greeting))
