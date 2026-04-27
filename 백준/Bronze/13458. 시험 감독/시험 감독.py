import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
b, c = map(int, sys.stdin.readline().rstrip().split())
res = 0

for i in range(n):
    lst[i] -= b
    res += 1
    if lst[i] > 0:
        if lst[i] % c == 0:
            res += lst[i] // c
        else:
            res += lst[i] // c + 1

print(res)