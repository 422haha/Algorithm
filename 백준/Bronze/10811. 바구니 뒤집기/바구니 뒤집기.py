import sys
n, m = map(int, sys.stdin.readline().split())
num = list(range(n+1))

for a in range(m):
    i, j = map(int, sys.stdin.readline().split())
    num[i:j+1] = num[i:j+1][::-1]

for b in range(1, n+1):
    print(num[b], end=' ')