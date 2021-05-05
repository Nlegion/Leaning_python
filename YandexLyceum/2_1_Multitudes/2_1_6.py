dishes = [input() for _ in range(int(input()))]
dishes_served = []
for _ in range(int(input())):
    dishes_served += [input() for _ in range(int(input()))]
for i in sorted(dishes):
    if i not in dishes_served:
        print(i)