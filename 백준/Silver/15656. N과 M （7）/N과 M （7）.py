import sys


def permutation_with_repetition(level):
    if level == m:
        print(*path)
        return
    for i in range(n):
        path.append(arr[i])
        permutation_with_repetition(level+1)
        path.pop()


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
path = []
permutation_with_repetition(0)