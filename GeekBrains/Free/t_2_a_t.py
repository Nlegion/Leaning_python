a = [2, 5, 8, 2, 12, 12, 4]
b = [2, 7, 12, 3]
for number in a[:]: #сделал срез списка
	if number in b:
			a.remove(number)
print (a)
