import sys


def combination(level, start):
    if level == m:
        print(*path)
        return
    for i in range(start, n+1):
        if used[i]:
            continue
        used[i] = 1
        path.append(i)
        combination(level+1, i+1)
        used[i] = 0
        path.pop()


n, m = map(int, sys.stdin.readline().rstrip().split())
path = []
used = [0]*(n+1)
combination(0, 1)