import sys


def combination(level, start):
    if level == m:
        print(*path)
        return
    for i in range(start, n):
        if used[i]:
            continue
        used[i] = 1
        path.append(arr[i])
        combination(level+1, i+1)
        used[i] = 0
        path.pop()


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
path = []
used = [0]*(n+1)
combination(0, 0)