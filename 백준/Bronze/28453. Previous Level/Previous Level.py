import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

for i in lst:
    if i < 250:
        print(4, end=' ')
    elif i < 275:
        print(3, end=' ')
    elif i < 300:
        print(2, end=' ')
    elif i == 300:
        print(1, end=' ')