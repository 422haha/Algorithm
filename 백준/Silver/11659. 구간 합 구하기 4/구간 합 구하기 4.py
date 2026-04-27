import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
sum_lst = [0] * len(lst)
sum_lst[0] = lst[0]
for i in range(1, len(lst)):
    sum_lst[i] = sum_lst[i-1] + lst[i]
for tc in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    if i == 1:
        print(sum_lst[j-1])
    else:
        print(sum_lst[j-1]-sum_lst[i-2])