import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
sum_lst = [0] * n
sum_lst[0] = lst[0]
for i in range(1, len(lst)):
    sum_lst[i] = sum_lst[i-1] + lst[i]

sum_lst_k = [0] * (n-k+1)
sum_lst_k[0] = sum_lst[k-1]
for i in range(1, n-k+1):
    sum_lst_k[i] = sum_lst[i+k-1] - sum_lst[i-1]

print(max(sum_lst_k))