def print_statistics(arr):
    if arr == []:
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
    else:
        print(len(arr))
        print(sum(arr) / len(arr))
        print(min(arr) / 1)
        print(max(arr) / 1)
        if len(arr) == 2:
            mean = arr[((len(arr)) // 2)]
            mean2 = arr[((len(arr)) // 2) - 1]
            print((mean + mean2) / 2)
        elif len(arr) % 2 == 0:
            mean = sorted(arr)[(len(arr)) // 2]
            mean2 = sorted(arr)[((len(arr)) // 2) - 1]
            print((mean + mean2) / 2)
        elif len(arr) == 1:
            print(arr[0] / 1)
        else:
            print(sorted(arr)[((len(arr) - 1) // 2 + 1) - 1])
