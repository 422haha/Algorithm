import sys


def nPm():
    if len(res) == m:
        print(*res)
        return
    else:
        for i in range(1, n+1):
            if visited[i]:
                continue
            else:
                visited[i] = 1
                res.append(i)
                nPm()
                res.pop()
                visited[i] = 0


n, m = map(int, sys.stdin.readline().rstrip().split())
lst = list(range(1, n+1))
res = []
visited = [0] * (n+1)
nPm()