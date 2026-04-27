import sys

n = int(input())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
res = 0
temp = 0

for i in range(n-1):
    if lst[i+1] > lst[i]:
        temp += lst[i+1] - lst[i]
    else:
        res = max(res, temp)
        temp = 0

print(max(res, temp))