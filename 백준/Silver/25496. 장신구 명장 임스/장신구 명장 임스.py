import sys

p, n = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst.sort()
temp = 200-p
cnt = 0
for i in range(n):
    if temp > 0:
        cnt += 1
        temp -= lst[i]
print(cnt)