import sys


def dfs(level, alst, blst):
    global res
    if level == n:
        if len(alst) == len(blst):
            a_sum = 0
            b_sum = 0
            for i in range(n//2):
                for j in range(n//2):
                    a_sum += arr[alst[i]][alst[j]]
                    b_sum += arr[blst[i]][blst[j]]
            res = min(res, abs(a_sum-b_sum))
        return
    dfs(level+1, alst+[level], blst)
    dfs(level+1, alst, blst+[level])


n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
res = 987654321
dfs(0, [], [])
print(res)