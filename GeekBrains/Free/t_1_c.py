user_name = input('Введите имя')
user_surname = input('Введите фамилию')
user_old = int(input('Введите возраст'))
user_ves = int(input('Введите вес'))
if (user_old <= 30) and ( 50 <= user_ves <= 120):
   print(user_name,' ',user_surname,'',user_old,'год','вес ',user_ves,'- хорошее состояние')
elif (30 > user_old < 39) and (( 50 < user_ves) or (user_ves > 120)):
   print(user_name,' ',user_surname,'',user_old,'год','вес ',user_ves,'- займитесь собой')
elif (user_old > 40) and (( 50 < user_ves) or (user_ves > 120)):
   print(user_name,' ',user_surname,'',user_old,'год','вес ',user_ves,'- займитесь собой')
else: print ('сам думай')
