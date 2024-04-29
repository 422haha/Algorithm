import sys
from collections import deque
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def bfs():
    global res
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
    dq = deque()
    dq.append((0, 0, 0))
    visited[0][0][0] = 1
    while dq:
        i, j, k = dq.popleft()
        if (i, j) == (n-1, m-1):
            return visited[n-1][m-1][k]
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj][k] == 0:
                if arr[ni][nj] == 0:
                    dq.append((ni, nj, k))
                    visited[ni][nj][k] = visited[i][j][k] + 1
                elif k == 0:
                    dq.append((ni, nj, 1))
                    visited[ni][nj][1] = visited[i][j][0] + 1
    return -1


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

print(bfs())