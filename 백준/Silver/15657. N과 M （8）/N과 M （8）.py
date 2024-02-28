import sys


def combination(level, start):
    if level == m:
        print(*path)
        return
    for i in range(start, n):
        path.append(arr[i])
        combination(level+1, i)
        path.pop()


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
path = []
combination(0, 0)