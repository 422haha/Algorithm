import sys

h, w, l = map(int, sys.stdin.readline().rstrip().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
word = list(sys.stdin.readline().rstrip())

dp = [[[0] * l for _ in range(w)] for _ in range(h)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

for i in range(h):
    for j in range(w):
        if arr[i][j] == word[0]:
            dp[i][j][0] = 1

for k in range(1, l):
    temp = word[k]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == temp:
                for di, dj in directions:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < h and 0 <= nj < w:
                        dp[i][j][k] += dp[ni][nj][k-1]

res = 0
for i in range(h):
    for j in range(w):
        res += dp[i][j][l-1]

print(res)