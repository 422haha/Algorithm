import sys
from collections import deque

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def check_for_start():
    global flag
    for i in range(n):
        for j in range(m):
            if flag == 0:
                if arr[i][j] == 0:
                    flag = 1
            if arr[i][j] == 1:
                dq.append((i, j))


def bfs():
    global day
    while dq:
        for i in range(len(dq)):
            x, y = dq.popleft()
            for d in range(4):
                nx = x + di[d]
                ny = y + dj[d]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    dq.append((nx, ny))


def check_for_result():
    day = -1
    for i in range(n):
        for j in range(m):
            if day < arr[i][j]:
                day = arr[i][j]
            if arr[i][j] == 0:
                return -1
    return day-1


m, n = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
flag = 0
dq = deque()
check_for_start()
if flag == 0:
    print(0)
else:
    bfs()
    print(check_for_result())