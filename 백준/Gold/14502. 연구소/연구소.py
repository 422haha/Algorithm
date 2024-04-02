import sys
from collections import deque
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def bfs(temp):
    dq = deque()
    cnt = len(lst)-3
    visited = [[0]*m for _ in range(n)]
    for i, j in temp:
        arr[i][j] = 1
    for i, j in virus:
        dq.append((i, j))
        visited[i][j] = 1
    while dq:
        i, j = dq.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < n and 0 <= nj < m:
                if visited[ni][nj] == 0 and arr[ni][nj] == 0:
                    visited[ni][nj] = 1
                    dq.append((ni, nj))
                    cnt -= 1
    for i, j in temp:
        arr[i][j] = 0
    return cnt


def dfs(level, temp):
    global res
    if level == 3:
        res = max(res, bfs(temp))
        return
    for i in range(len(lst)):
        if visited_wall[i] == 0:
            visited_wall[i] = 1
            dfs(level+1, temp+[lst[i]])
            visited_wall[i] = 0


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

lst = []
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            lst.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

visited_wall = [0]*len(lst)
res = 0
dfs(0, [])

print(res)