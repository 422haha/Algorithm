import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
lst = list(range(n+1))
lst[1] = 0
cnt = 0
res = 0
for i in range(2, n+1):
    if lst[i] == 0:
        continue
    j = 1
    while i*j <= n:                 # 에라토스테네스의 체
        if lst[i*j] != 0:
            lst[i*j] = 0
            cnt += 1
            if cnt == k:
                res = i*j
                break
        j += 1
    if cnt == k:                    # 값을 찾으면 break
        break

print(res)