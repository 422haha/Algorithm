import sys
from heapq import heappop, heappush

k, n = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
res = []

for i in lst:
    heappush(res, i)

for i in range(n):
    temp = heappop(res)
    for j in range(k):
        heappush(res, temp*lst[j])
        if temp % lst[j] == 0:
            break

print(temp)