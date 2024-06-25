import sys
import math


def prime(x):
    for j in range(2, int(math.sqrt(x)+1)):
        if x % j == 0:
            return False
    return True


n = int(sys.stdin.readline().rstrip())

for i in range(n, 1003002):
    if i == 1:
        continue
    if str(i) == str(i)[::-1]:
        if prime(i):
            print(i)
            sys.exit(0)