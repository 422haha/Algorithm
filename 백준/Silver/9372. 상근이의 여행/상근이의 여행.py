import sys

t = int(sys.stdin.readline().rstrip())
for tc in range(1, t+1):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
    print(n-1)