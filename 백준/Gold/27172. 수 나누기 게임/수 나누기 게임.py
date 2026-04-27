import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

dct = {}
for i in range(n):
    dct[lst[i]] = i
max_ = max(lst)
res = [0]*n

for i in range(n):
    now = lst[i]
    for j in range(now*2, max_+1, now):
        if j in dct:
            res[i] += 1
            res[dct[j]] -= 1

for i in res:
    print(i, end=' ')