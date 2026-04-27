import sys

n, m = map(int, sys.stdin.readline().split())
dct = {}
cnt = 0
for i in range(n):
    dct[sys.stdin.readline().rstrip()] = 1
for j in range(m):
    if sys.stdin.readline().rstrip() in dct:
        cnt += 1
print(cnt)