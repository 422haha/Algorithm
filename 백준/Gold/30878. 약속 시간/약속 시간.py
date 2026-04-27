import sys
from math import gcd

m = int(sys.stdin.readline().rstrip())
a = m * m * (90 - m)
b = 108000
g = gcd(a, b)

print(f"{a // g}/{b // g}")