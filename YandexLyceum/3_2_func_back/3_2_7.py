def find_mountain(heightsMap):
    row = -1
    maxValue = 0
    for i in heightsMap:
        if max(i) > maxValue:
            maxValue = max(i)
    for i in heightsMap:
        row += 1
        column = -1
        for j in i:
            column += 1
            if j == maxValue:
                return row, column
