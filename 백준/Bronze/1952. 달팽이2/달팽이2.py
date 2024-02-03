import sys
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

m, n = map(int, sys.stdin.readline().rstrip().split())
arr = [[0]*n for _ in range(m)]
ni = 0
nj = 0
dr = 0
cnt = 1
res = 0
while cnt < m*n:
    if 0 <= ni+di[dr] < m and 0 <= nj+dj[dr] < n and arr[ni+di[dr]][nj+dj[dr]] == 0:
        arr[ni][nj] = cnt
        ni += di[dr]
        nj += dj[dr]
        cnt += 1
    else:
        dr = (dr+1) % 4
        res += 1
print(res)