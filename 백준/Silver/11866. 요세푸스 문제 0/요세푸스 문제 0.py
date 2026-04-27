import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
lst = [i for i in range(1, n+1)]
lst = deque(lst)
res = []
for i in range(n):
    for j in range(k-1):
        lst.append(lst.popleft())
    res.append(lst.popleft())
print('<', end='')
for i in range(n-1):
    print(f'{res[i]}, ', end='')
print(f'{res[n-1]}>')