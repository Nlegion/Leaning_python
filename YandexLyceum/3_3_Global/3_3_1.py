def circle_length(radius):
    p = 3.14159
    return radius * p * 2


def circle_area(radius):
    p = 3.14159
    return p * radius ** 2


def main():
    r = float(input())
    p = 3.14159
    print(r * p * 2, p * r ** 2)
