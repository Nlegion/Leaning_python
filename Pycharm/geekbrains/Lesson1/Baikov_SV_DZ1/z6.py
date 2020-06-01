a = 2
b = 3
c = 1
percent = 10

while b >= a:
    a = a + (a * (percent / 100))
    c = c + 1
print('на {0}-й день спортсмен достиг результата — не менее {1} км.'.format(c,b))

