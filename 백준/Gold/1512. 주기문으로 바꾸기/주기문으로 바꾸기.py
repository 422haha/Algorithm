import sys

m = int(sys.stdin.readline().rstrip())
s = list(map(str, sys.stdin.readline().rstrip()))
n = len(s)
res = 1e9

for i in range(1, m+1):
    temp = 0
    for j in range(i):
        cnt = [0]*4
        total = 0
        for k in range(j, n, i):
            if s[k] == 'A':
                cnt[0] += 1
            elif s[k] == 'C':
                cnt[1] += 1
            elif s[k] == 'G':
                cnt[2] += 1
            elif s[k] == 'T':
                cnt[3] += 1
            total += 1
        max_cnt = max(cnt)
        temp += total - max_cnt
    res = min(res, temp)

print(res)