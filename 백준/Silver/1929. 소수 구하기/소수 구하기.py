import sys
import math

def prime(num):
    if num == 0 or num == 1:
        return False
    if num == 2:
        return 2
    sq = math.ceil((math.sqrt(num)))
    for i in range(2, sq+1):
        if num % i == 0:
            return False
    return num


n, m = map(int, sys.stdin.readline().rstrip().split())
lst = []
for i in range(n, m+1):
    res = prime(i)
    if res:
        lst.append(res)
for i in lst:
    print(i)