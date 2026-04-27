import math
import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == '0':
        break
    n = len(s)
    res = 0
    for i in range(n):
        res += int(s[i])*math.factorial(n-i)
    print(res)