import sys


def check():
    bingo = 0
    # |대각선 체크
    ck = 0
    for i in range(5):
        if board[i][i] == 1:
            ck += 1
    if ck == 5:
        bingo += 1
    # /대각선 체크
    ck = 0
    for i in range(5):
        if board[i][4-i] == 1:
            ck += 1
    if ck == 5:
        bingo += 1
    # i줄 체크
    for i in range(5):
        ck = 0
        for j in range(5):
            if board[i][j] == 1:
                ck += 1
        if ck == 5:
            bingo += 1
    # j줄 체크
    for j in range(5):
        ck = 0
        for i in range(5):
            if board[i][j] == 1:
                ck += 1
        if ck == 5:
            bingo += 1
    return bingo


arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(5)]
ans = []
for i in range(5):
    ans += map(int, sys.stdin.readline().rstrip().split())
bingo = 0
cnt = 0
board = [[0]*5 for _ in range(5)]

while bingo < 3:
    for i in range(5):
        for j in range(5):
            if arr[i][j] == ans[cnt]:
                board[i][j] = 1
    bingo = check()
    cnt += 1

print(cnt)