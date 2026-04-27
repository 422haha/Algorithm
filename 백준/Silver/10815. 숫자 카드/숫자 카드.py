import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
dct = {}
for i in lst:
    dct[i] = 1
m = int(sys.stdin.readline())
check_lst = list(map(int, sys.stdin.readline().rstrip().split()))
for j in check_lst:
    if j in dct:
        print(1, end=' ')
    else:
        print(0, end=' ')