import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst_n = list(map(int, sys.stdin.readline().rstrip().split()))
lst_o = list(map(int, sys.stdin.readline().rstrip().split()))
sum_n = n
sum_o = m

lst_n.sort()
lst_o.sort()
temp_n = lst_n[0]
temp_o = lst_o[0]

for i in range(n - 1):
    if lst_n[i] - temp_n >= 100:
        temp_n = lst_n[i]
    else:
        sum_n -= 1

for i in range(m - 1):
    if lst_o[i] - temp_o >= 360:
        temp_o = lst_o[i]
    else:
        sum_o -= 1

print(sum_n, sum_o)