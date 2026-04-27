import sys
import heapq

n, k = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
bags = [int(sys.stdin.readline().rstrip()) for _ in range(k)]
arr.sort()
bags.sort()

res = 0
temp = []
for bag in bags:
    while arr and arr[0][0] <= bag:
        heapq.heappush(temp, (-1) * arr[0][1])  # 보석의 가치를 음수로 변환하여 최대 힙에 저장
        heapq.heappop(arr)
    if temp:
        res -= heapq.heappop(temp)  # 최대 힙에서 가장 가치가 높은 보석을 선택하여 res에 더함
print(res)