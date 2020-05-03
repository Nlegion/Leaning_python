def unlucky_number (number):
   if number == 13:
       raise ValueError('Несчастливое число')
   else:
       return number ** 2

number = int(input('введите число'))

result = unlucky_number(number)
