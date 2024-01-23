import sys
n = int(sys.stdin.readline())
cnt = 0

for i in range(n):
    lst = list(sys.stdin.readline())
    set_len = len(set(lst))
    lst_f = 0
    for j in range(len(lst)):
        if lst[j] != lst[j-1]:
            lst_f += 1
    if lst_f == set_len:
        cnt += 1

print(cnt)