basket = ['159.5', '789.2', '647.7']
#изменяемость объекта

print(id(basket),basket)
basket[0] = 879
print(basket)

basket = tuple(basket) # объявление кортежа
