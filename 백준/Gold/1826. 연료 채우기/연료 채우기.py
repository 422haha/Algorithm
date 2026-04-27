import sys
import heapq

n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n+1)]
arr.sort(key=lambda x:(x[0], -x[1]))
energy = arr[n][1]
now = 0
cnt = 0

hq = []                 # 최댓값 찾기
for i in range(n+1):
    d = arr[i][0] - now
    now = arr[i][0]
    if energy < d:      # 연료가 부족할 때 이전의 정류장 중 연료량 제일 많은곳 찾음
        while energy < d:
            if len(hq) > 0:
                energy += (-1)*heapq.heappop(hq)
                cnt += 1
            else:
                cnt = -1
                break
        if cnt == -1:   # 마을에 도착하지 못함
            break
    energy -= d
    heapq.heappush(hq, (-1)*arr[i][1])  # (-1)을 곱하면 최댓값 찾기 쉬워짐
print(cnt)