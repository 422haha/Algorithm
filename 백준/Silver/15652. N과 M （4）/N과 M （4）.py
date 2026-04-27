import sys


def combination(level, start):
    if level == m:
        print(*path)
        return
    for i in range(start, n+1):
        path.append(i)
        combination(level+1, i)
        path.pop()


n, m = map(int, sys.stdin.readline().rstrip().split())
path = []
combination(0, 1)