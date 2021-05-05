cislo = int(input())
hod = 0
while cislo != 1:
    if cislo % 2 == 0:
        cislo /= 2
    elif cislo % 2 == 1:
        cislo -= 1
    hod += 1
print(hod)