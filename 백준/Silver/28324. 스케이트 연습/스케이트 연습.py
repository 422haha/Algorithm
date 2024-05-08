import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
res = 0
now = 0
for i in range(n-1, -1, -1):
    if lst[i]-now >= 1:
        now += 1
    elif lst[i]-now < 0:
        now = lst[i]
    res += now
print(res)