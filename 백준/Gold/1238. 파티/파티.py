import sys
from heapq import heappush, heappop


def dijkstra(s):
    pq = []
    # 시작점의 weight, node 번호를 한 번에 저장
    heappush(pq, (0, s))
    # 시작 노드 초기화
    visited[s] = 0  # 시작점 초기화 안하면 사이클 발생할 수 있음
    while pq:
        d, n = heappop(pq)
        # n이 이미 더 짧은 거리로 온 적이 있다면 pass
        if visited[n] < d:
            continue
        # 현재 인접한 다른 노드
        for w in arr[n]:
            wd, wn = w
            # 누적 거리 계산
            wd = d + wd
            # 이미 더 짧은 거리로 간 경우 pass
            if wd >= visited[wn]:
                continue
            visited[wn] = wd
            heappush(pq, (wd, wn))


inf = int(1e9)  # 거리 다 더한 값보다 커야함
n, m, x = map(int, sys.stdin.readline().rstrip().split())

# 인접 리스트
arr = [[] for _ in range(n+1)]
# 누적 거리를 저장할 변수
visited = [inf] * (n+1)
# 간선 정보 저장
for _ in range(m):
    s, f, d = map(int, sys.stdin.readline().rstrip().split())
    arr[s].append([d, f])
dijkstra(x)
temp = visited[:]
res = 0
for i in range(1, n+1):
    visited = [inf] * (n + 1)
    dijkstra(i)
    time = visited[x] + temp[i]
    if res < time:
        res = time
print(res)