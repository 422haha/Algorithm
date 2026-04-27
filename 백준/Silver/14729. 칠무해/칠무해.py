import sys
import heapq

n = int(sys.stdin.readline().rstrip())
lst = []

for i in range(n):
    heapq.heappush(lst, float(sys.stdin.readline().rstrip()))

for _ in range(7):
    print('{:.3f}'.format(heapq.heappop(lst)))