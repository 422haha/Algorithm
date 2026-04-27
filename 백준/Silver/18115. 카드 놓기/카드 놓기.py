import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst.reverse()
res = deque()

for i in range(n):
    if lst[i] == 1:
        res.appendleft(i+1)
    if lst[i] == 2:
        res.insert(1, i+1)
    if lst[i] == 3:
        res.append(i+1)

print(*res)