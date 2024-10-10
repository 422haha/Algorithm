import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def check(x, y):
    lcm_value = lcm(lcm(4, 2), lcm(3, 5))

    for year in range(x, y + 1):
        if (year - x) % lcm_value == 0:
            print(f"All positions change in year {year}")


x = int(input())
y = int(input())
check(x, y)