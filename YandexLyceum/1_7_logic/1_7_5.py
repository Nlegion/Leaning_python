price1 = int(input())
price2 = int(input())
in_stock = False
while price2 != 0:
    if not in_stock:
        if price1 < price2:
            inprice = price2
            in_stock = True
    if in_stock:
        if price1 > price2:
            outprice = price2
            break
    price1 = price2
    price2 = int(input())
print(inprice, outprice, outprice - inprice)
