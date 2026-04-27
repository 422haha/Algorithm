import sys
import heapq

n = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    heapq.heappush(lst, num)

res = 0
while len(lst) > 1:
    n1 = heapq.heappop(lst)
    n2 = heapq.heappop(lst)
    res += n1+n2
    heapq.heappush(lst, n1+n2)

print(res)