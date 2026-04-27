import sys

arr = [list(map(str, sys.stdin.readline().rstrip().split())) for _ in range(10)]
res = 0
for i in range(10):     # 행 검사
    temp = arr[i][0]
    flag = 1
    for j in range(10):
        if arr[i][j] != temp:
            flag = 0
    if flag == 1:
        res = 1
for i in range(10):     # 열 검사
    temp = arr[0][i]
    flag = 1
    for j in range(10):
        if arr[j][i] != temp:
            flag = 0
    if flag == 1:
        res = 1
print(res)