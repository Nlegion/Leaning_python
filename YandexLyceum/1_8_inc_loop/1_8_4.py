max_height = -1
max_road = None
for road in range(1, int(input()) + 1):
    min_height = min(int(input()) for _ in range(int(input())))
    if min_height > max_height:
        max_height = min_height
        max_road = road
print(max_road, max_height)