import sys


def dfs(day, cursum):
    global res
    if day >= n:
        if res < cursum:
            res = cursum
        return
    dfs(day+1, cursum)
    if day+T[day] <= n:
        dfs(day+T[day], cursum+P[day])


n = int(sys.stdin.readline())
T = [0]*n
P = [0]*n
for i in range(n):
    T[i], P[i] = map(int, sys.stdin.readline().split())

res = 0
dfs(0, 0)

print(res)