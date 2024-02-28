import sys


def permutation_with_repetition(level):
    if level == m:
        print(*path)
        return
    for i in range(1, n+1):
        path.append(i)
        permutation_with_repetition(level+1)
        path.pop()


n, m = map(int, sys.stdin.readline().rstrip().split())
path = []
permutation_with_repetition(0)