my_list_1 = [2, 2, 5, 12, 8, 2, 12]
z = ''
for i in my_list_1:
   z = i
   for j in my_list_1:
       if z == j:
           my_list_1.remove(i)
print(my_list_1)
