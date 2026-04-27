import sys
from collections import deque
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

n, m, l = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

visited = [[[0]*(l+1) for _ in range(m)] for _ in range(n)]
dq = deque()
dq.append((0, 0, 0, 1))
visited[0][0][0] = 1

while dq:
    i, j, k, day = dq.popleft()
    if (i, j) == (n-1, m-1):
        print(day)
        sys.exit(0)
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < n and 0 <= nj < m:
            if arr[ni][nj] == 0 and visited[ni][nj][k] == 0:
                dq.append((ni, nj, k, day+1))
                visited[ni][nj][k] = day
            elif k < l and visited[ni][nj][k+1] == 0:
                if day % 2 != 0:
                    dq.append((ni, nj, k+1, day+1))
                    visited[ni][nj][k+1] = day
                else:
                    dq.append((i, j, k, day+1))
print(-1)