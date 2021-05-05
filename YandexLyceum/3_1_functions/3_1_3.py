def quarter(x, y):
    ans = [['I', 'II'], ['IV', 'III']]
    print(ans[y < 0][x < 0], 'четверть')
