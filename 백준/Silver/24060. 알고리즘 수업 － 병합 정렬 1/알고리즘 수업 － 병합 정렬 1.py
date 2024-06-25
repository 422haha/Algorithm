import sys
from collections import deque


def merge_sort(p, r):
    global cnt, res
    if p < r:
        q = (p+r) // 2
        merge_sort(p, q)
        merge_sort(q+1, r)
        merge(p, q, r)


def merge(p, q, r):
    global cnt, res
    i = p
    j = q + 1
    t = p

    while i <= q and j <= r:
        if lst[i] <= lst[j]:
            temp[t] = lst[i]
            i += 1
        else:
            temp[t] = lst[j]
            j += 1
        t += 1

    while i <= q:
        temp[t] = lst[i]
        i += 1
        t += 1

    while j <= r:
        temp[t] = lst[j]
        j += 1
        t += 1

    for i in range(p, r+1):
        lst[i] = temp[i]
        cnt += 1
        if cnt == k:
            res = lst[i]


n, k = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
res = -1

temp = [0] * n
merge_sort(0, n-1)

print(res)