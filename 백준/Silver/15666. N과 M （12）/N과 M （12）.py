import sys


def combination_with_repetition(level, start):
    if level == m:
        print(*path)
        return
    for i in range(start, len(arr)):
        path.append(arr[i])
        combination_with_repetition(level+1, i)
        path.pop()


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr = list(set(arr))
arr.sort()
path = []
combination_with_repetition(0, 0)