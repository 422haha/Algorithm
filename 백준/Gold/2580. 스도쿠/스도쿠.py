import sys


def check_r(r, k):            # 해당 행에 중복된 숫자가 있는지 확인하는 함수
    for i in range(9):
        if arr[r][i] == k:
            return False
    return True


def check_c(c, k):            # 해당 열에 중복된 숫자가 있는지 확인하는 함수
    for i in range(9):
        if arr[i][c] == k:
            return False
    return True


def check_s(r, c, k):         # 해당 3x3 사각형에 중복된 숫자가 있는지 확인하는 함수
    start_r = r // 3 * 3
    start_c = c // 3 * 3
    for i in range(3):
        for j in range(3):
            if arr[start_r + i][start_c + j] == k:
                return False
    return True


def dfs(n):
    if n == len(temp):
        for row in arr:
            print(*row)
        sys.exit(0)
    r, c = temp[n]
    for k in range(1, 10):
        if check_r(r, k) and check_c(c, k) and check_s(r, c, k):
            arr[r][c] = k
            dfs(n + 1)
            arr[r][c] = 0


arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
temp = []

for i in range(9):              # 빈 칸의 좌표 저장
    for j in range(9):
        if arr[i][j] == 0:
            temp.append((i, j))

dfs(0)