import sys
di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]
cloud_i = [1, -1, 1, -1]
cloud_j = [1, 1, -1, -1]

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for _ in range(m):
    d, s = map(int, sys.stdin.readline().rstrip().split())
    reproduction = []
    for i, j in cloud:
        ni = (i + di[d-1]*s + n) % n
        nj = (j + dj[d-1]*s + n) % n
        arr[ni][nj] += 1
        reproduction.append((ni, nj))
    cloud = []
    for i, j in reproduction:
        for d in range(4):
            ni = i + cloud_i[d]
            nj = j + cloud_j[d]
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] > 0:
                    arr[i][j] += 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and (i, j) not in reproduction:
                arr[i][j] -= 2
                cloud.append((i, j))

res = 0
for lst in arr:
    res += sum(lst)
print(res)