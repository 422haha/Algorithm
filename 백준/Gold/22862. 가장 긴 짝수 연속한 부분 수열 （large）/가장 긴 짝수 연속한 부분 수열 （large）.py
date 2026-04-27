import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

end, now, cnt, res = 0, 0, 0, 0

for i in range(n):
    while end < n and cnt <= k:
        if lst[end] % 2 == 0:
            now += 1
        else:
            cnt += 1
        end += 1
        if cnt > k:
            break
        res = max(res, now)
    if lst[i] % 2 == 0:
        now -= 1
    else:
        cnt -= 1

print(res)