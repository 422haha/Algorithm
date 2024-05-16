import sys

n, d = map(int, sys.stdin.readline().rstrip().split())
d = str(d)

res = 0
for i in range(1, n+1):
    res += str(i).count(d)

print(res)