import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]

# 보드와 부분합 배열 초기화
board = [[0]*(n+1) for _ in range(n+1)]
psum = [[0]*(n+1) for _ in range(n+1)]

# 블록 위치 설정 및 부분합 배열 계산
for x, y in arr:
    board[x][y] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        psum[i][j] = psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1] + board[i][j]

# 가능한 모든 직사각형 크기(a, b)에 대해 최소 움직임 수 계산
res = m
for a in range(1, m+1):
    if m % a != 0:
        continue
    b = m // a
    for x1 in range(1, n-a+2):
        for y1 in range(1, n-b+2):
            # 부분합을 이용하여 특정 영역의 합을 계산
            area_sum = psum[x1+a-1][y1+b-1] - psum[x1-1][y1+b-1] - psum[x1+a-1][y1-1] + psum[x1-1][y1-1]
            res = min(res, m-area_sum)

print(res)