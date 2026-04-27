import sys
from itertools import combinations


def mbti_d(p1, p2):
    d = 0
    for i, j in zip(p1, p2):
        if i != j:
            d += 1
    return d


t = int(sys.stdin.readline())

for tc in range(1, t+1):
    n = int(sys.stdin.readline())
    arr = list(map(str, sys.stdin.readline().rstrip().split()))
    if n > 32:
        print(0)
        continue
    
    min_ = 100001
    lst = combinations(arr, 3)
    for x, y, z in lst:
        res = 0
        res += mbti_d(x, y)
        res += mbti_d(x, z)
        res += mbti_d(y, z)
        min_ = min(min_, res)
    print(min_)