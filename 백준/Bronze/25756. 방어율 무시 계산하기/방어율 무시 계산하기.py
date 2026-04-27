import sys

n = int(sys.stdin.readline())
lst = list(map(float, sys.stdin.readline().rstrip().split()))
ignore = 0

for i in range(n):
    ignore = 1 - (1 - ignore) * (1 - lst[i] / 100)
    print(round(ignore * 100, 6))