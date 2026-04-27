import sys

t = int(sys.stdin.readline())
for tc in range(1, t+1):
    n = int(sys.stdin.readline())
    dct = {}
    for i in range(n):
        r, c = map(str, sys.stdin.readline().rstrip().split())
        if c in dct:
            dct[c] += 1
        else:
            dct[c] = 1
    lst = dct.values()
    res = 1
    for i in lst:
        res *= (i+1)
    print(res-1)