import sys


def combination(level):
    if level == m:
        print(*path)
        return
    temp = 0
    for i in range(n):
        if used[i] or temp == arr[i]:
            continue
        used[i] = 1
        path.append(arr[i])
        temp = arr[i]
        combination(level+1)
        used[i] = 0
        path.pop()


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
path = []
used = [0]*(n+1)
combination(0)