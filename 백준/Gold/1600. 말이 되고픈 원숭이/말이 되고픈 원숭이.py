import sys
from collections import deque
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
hi = [-2, -2, -1, -1, 1, 1, 2, 2]
hj = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs():
    visited = [[[0]*(l+1) for _ in range(m)] for _ in range(n)]
    dq = deque()
    dq.append((0, 0, 0))
    visited[0][0][0] = 1
    while dq:
        i, j, k = dq.popleft()
        if (i, j) == (n-1, m-1):
            return visited[n-1][m-1][k]-1
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 0 and visited[ni][nj][k] == 0:
                    dq.append((ni, nj, k))
                    visited[ni][nj][k] = visited[i][j][k] + 1
        if k < l:
            for d in range(8):
                ni = i + hi[d]
                nj = j + hj[d]
                if 0 <= ni < n and 0 <= nj < m:
                    if arr[ni][nj] == 0 and visited[ni][nj][k+1] == 0:
                        dq.append((ni, nj, k+1))
                        visited[ni][nj][k+1] = visited[i][j][k] + 1
    return -1


l = int(sys.stdin.readline().rstrip())
m, n = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

print(bfs())