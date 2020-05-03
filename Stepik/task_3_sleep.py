A = int(input()) #минимум
B = int(input()) #максимум
H = int(input()) #сейчас
if (H <= B) and (H >= A):
    print('Это нормально')
elif H <= A:
    print('Недосып')
else:
    print ('Пересып')
