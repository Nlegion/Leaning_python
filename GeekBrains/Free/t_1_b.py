while True:
   user_an = int(input('Введите число от 0 до 9'))
   if 0 <= user_an <= 9:
       print (user_an ** 2)
   else:
       user_an = int(input('Неверное число. Введите число от 0 до 9'))
