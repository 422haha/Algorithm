import sys
n = list(map(int, sys.stdin.readline().rstrip()))
n.sort(reverse=True)

for i in n:
    print(i, end='')