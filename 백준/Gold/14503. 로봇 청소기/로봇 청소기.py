import sys

di = [-1, 0, 1, 0]              # 북, 동, 남, 서
dj = [0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().rstrip().split())
i, j, d = map(int, sys.stdin.readline().rstrip().split())   # 0 : 북, 1 : 동, 2 : 남, 3 : 서
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

visited[i][j] = 1
cnt = 1

while True:
    flag = 0
    for _ in range(4):
        d -= 1          # 왼쪽 회전
        if d == -1:     # -1이되면 3으로 바꿔줌
            d = 3
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
            if visited[ni][nj] == 0:
                visited[ni][nj] = 1
                cnt += 1
                i, j = ni, nj
                flag = 1
                break
    if flag == 0:
        if arr[i-di[d]][j-dj[d]] == 1:
            print(cnt)
            sys.exit(0)
        else:
            i, j = i-di[d], j-dj[d]