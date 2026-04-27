import sys
from math import sqrt

n = int(sys.stdin.readline().rstrip())
res = n

for i in range(2, int(sqrt(n))+1):
    if n % i == 0:
        while n % i == 0:
            n //= i
        res *= (1-1/i)

if n > 1:
    res *= (1-1/n)

print(int(res))