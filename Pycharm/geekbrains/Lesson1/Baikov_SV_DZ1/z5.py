#deb = int(input('введите выручку'))
#cre = int(input('введите издержки'))

deb = 10000
cre = 9000
bal = deb - cre
if bal > 0:
    print('выручка больше издержек')
    print('рентабильность выручки: %.2f' % ((bal / deb) * 100), ' процентов')
    # sot =  int(input('количество сотрудников'))
    sot = 10
    print ('прибыль фирмы в расчете на одного сотрудника: %.2f' % (bal/sot))
elif bal < 0:
    print('издержки больше выручки')
else:
    print('издержки равны выручке')