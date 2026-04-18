import sys
import math

for _ in range(int(sys.stdin.readline())):
    x, w = map(int, sys.stdin.readline().split())
    if w <= x:
        res = 0
    else:
        res = math.ceil(math.log2(w/x))
    print(res)