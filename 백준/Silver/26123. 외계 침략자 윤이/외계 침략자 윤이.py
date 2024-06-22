import sys
from collections import defaultdict

n, d = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

dct = defaultdict(int)
for i in lst:
    dct[i] += 1
max_height = max(dct.keys())

res = 0

while d > 0 and max_height > 0:
    cnt = dct[max_height]
    res += cnt
    max_height -= 1
    dct[max_height] += cnt
    d -= 1

print(res)