import sys

n, m = map(int, sys.stdin.readline().split())
dct = {}
for _ in range(n):
    lst = list(sys.stdin.readline().rstrip().split())
    dct[lst[0]] = lst[1]
for _ in range(m):
    site = sys.stdin.readline().rstrip()
    print(dct[site])