import sys


def dfs(n, cnt):
    global res
    if n == num:
        if res < cnt:
            res = cnt
        return
    if arr[n][0] <= 0:
        dfs(n+1, cnt)
    else:
        flag = 0
        for i in range(num):
            if n == i or arr[i][0] <= 0:
                continue
            flag = 1
            arr[n][0] -= arr[i][1]
            arr[i][0] -= arr[n][1]
            dfs(n+1, cnt + int(arr[n][0] <= 0) + int(arr[i][0] <= 0))
            arr[n][0] += arr[i][1]
            arr[i][0] += arr[n][1]
        if flag == 0:
            dfs(n+1, cnt)


num = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(num)]
res = 0
dfs(0, 0)
print(res)