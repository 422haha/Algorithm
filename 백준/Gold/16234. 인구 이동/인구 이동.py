import sys
from collections import deque
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


n, l, r = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
res = 0
while res <= 2000:
    flag = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                dq = deque()
                dq.append((i, j))
                temp_arr = []
                temp = 0
                temp_arr.append((i, j))
                temp += arr[i][j]
                visited[i][j] = 1
                while dq:
                    ci, cj = dq.popleft()
                    for d in range(4):
                        ni = ci + di[d]
                        nj = cj + dj[d]
                        if 0 <= ni < n and 0 <= nj < n:
                            if visited[ni][nj] == 0 and l <= abs(arr[ci][cj] - arr[ni][nj]) <= r:
                                temp += arr[ni][nj]
                                temp_arr.append((ni, nj))
                                visited[ni][nj] = 1
                                dq.append((ni, nj))
                if len(temp_arr) > 1:
                    for ci, cj in temp_arr:
                        arr[ci][cj] = temp // len(temp_arr)
                        flag = 1
    if flag == 0:
        break
    res += 1
print(res)