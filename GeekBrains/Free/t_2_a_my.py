my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
z = 1
while (z != 0):
   z =0
   for i in my_list_1:
       for j in my_list_2:
           if i == j:
               z = z + 1
               my_list_1.remove(i)
print(my_list_1)