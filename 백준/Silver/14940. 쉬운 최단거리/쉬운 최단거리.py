import sys
from collections import deque


def bfs(si, sj):
    dq = deque([(si, sj)])
    visited[si][sj] = 0
    while dq:
        ni, nj = dq.popleft()
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            wi = di + ni
            wj = dj + nj
            if 0 <= wi < n and 0 <= wj < m and visited[wi][wj] == -1:
                visited[wi][wj] = visited[ni][nj] + 1
                dq.append((wi, wj))


n, m = map(int, sys.stdin.readline().rstrip().split())
visited = [[-1]*m for _ in range(n)]
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
si, sj = 0, 0                   # 시작 지점 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            visited[i][j] = 0
        if arr[i][j] == 2:
            si, sj = i, j
bfs(si, sj)
for i in visited:
    print(*i)