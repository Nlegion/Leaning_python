import math


def discriminant(a, b, c):
    return b * b - 4 * a * c


def smaller_root(p, q):
    return p * -0.5 - math.sqrt(p ** 2 / 4 - q)


def larger_root(p, q):
    return p * -0.5 + math.sqrt(p ** 2 / 4 - q)


def main():
    p = float(input())
    q = float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))
