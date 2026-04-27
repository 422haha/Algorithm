import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = {}
for i in lst:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

m = int(sys.stdin.readline())
lst_2 = list(map(int, sys.stdin.readline().rstrip().split()))
for i in lst_2:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')