import sys

n = int(sys.stdin.readline().rstrip())
lst = [str(sys.stdin.readline().rstrip()) for _ in range(n)]
idx = [i for i in range(n+1)]
next = [i for i in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    idx[next[a]] = b
    next[a] = next[b]

for _ in range(n):
    print(lst[a-1], end='')
    a = idx[a]