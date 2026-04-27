import sys
from collections import deque
from itertools import combinations
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def bfs(temp):
    dq = deque()
    cnt = 0
    count = 0
    visited = [[0]*n for _ in range(n)]
    for i, j in temp:
        dq.append((i, j))
        visited[i][j] = 1
    while dq:
        i, j = dq.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < n and 0 <= nj < n:
                if visited[ni][nj] == 0 and arr[ni][nj] != 1:
                    visited[ni][nj] = visited[i][j] + 1
                    dq.append((ni, nj))
                    count += 1
                    cnt = max(cnt, visited[ni][nj])
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and arr[i][j] != 1:
                return inf
    return cnt


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
inf = int(1e9)
res = inf

flag = 0
virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus.append((i, j))
        elif arr[i][j] != 1:
            flag = 1

for selected_virus in combinations(virus, m):
    res = min(res, bfs(selected_virus))

if res == inf:
    res = 0
if flag == 0 and res == 0:
    if m < len(virus):
        print(-1)
    else:
        print(0)
else:
    print(res-1)