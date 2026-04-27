import sys
from math import sqrt, gcd

g, l = map(int, sys.stdin.readline().rstrip().split())
n = l // g

for i in range(int(sqrt(n)), 0, -1):
    if n % i == 0:
        x = g * i
        y = g * (n//i)
        if gcd(x, y) == g:
            print(x, y)
            sys.exit(0)