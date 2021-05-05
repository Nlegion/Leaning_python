def fact_2(n):
    p = 1
    for i in range(2, n + 1):
        p *= i
    return p


print(fact_2(int(input())))
