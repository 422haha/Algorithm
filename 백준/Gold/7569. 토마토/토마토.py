import sys
from collections import deque

di = [1, -1, 0, 0, 0, 0]
dj = [0, 0, 1, -1, 0, 0]
dk = [0, 0, 0, 0, 1, -1]


def check_for_start():
    global flag
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if flag == 0:
                    if arr[k][i][j] == 0:
                        flag = 1
                if arr[k][i][j] == 1:
                    dq.append((k, i, j))


def bfs():
    while dq:
        for i in range(len(dq)):
            z, x, y = dq.popleft()
            for d in range(6):
                nx = x + di[d]
                ny = y + dj[d]
                nz = z + dk[d]
                if 0 <= nz < h  and 0 <= nx < n and 0 <= ny < m and arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = arr[z][x][y] + 1
                    dq.append((nz, nx, ny))


def check_for_result():
    day = -1
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if day < arr[k][i][j]:
                    day = arr[k][i][j]
                if arr[k][i][j] == 0:
                    return -1
    return day-1


m, n, h = map(int, sys.stdin.readline().rstrip().split())
arr = []
for k in range(h):
    arr.append([list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)])
flag = 0
dq = deque()
check_for_start()
if flag == 0:
    print(0)
else:
    bfs()
    print(check_for_result())