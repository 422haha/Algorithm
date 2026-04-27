import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst.sort()

max_dif = 0
res = -1

for i in range(1, n):
    dif = (lst[i] - lst[i-1]) // 2

    if max_dif < dif:
        max_dif = dif
        res = (lst[i] + lst[i-1]) // 2

print(res)