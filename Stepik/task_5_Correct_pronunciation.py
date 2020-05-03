n = int (input())
if (n%10) == 1 and (n%100) != 11 :
    print (n,'программист')
elif 2 <= (n%10) <= 4 and (n%100) != 12 and (n%100) != 13 and (n%100) != 14:
    print (n,'программиста')
else:
    print (n,'программистов')
