import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
g_lst = [0]*6
b_lst = [0]*6
cnt = 0

for i in range(n):
    s, y = map(int, sys.stdin.readline().rstrip().split())
    if s == 0:
        g_lst[y-1] += 1
    else:
        b_lst[y-1] += 1

for i in range(6):
    if g_lst[i]:
        if g_lst[i] % k == 0:
            cnt += g_lst[i]//k
        else:
            cnt += g_lst[i]//k + 1
    if b_lst[i]:
        if b_lst[i] % k == 0:
            cnt += b_lst[i] // k
        else:
            cnt += b_lst[i]//k + 1

print(cnt)