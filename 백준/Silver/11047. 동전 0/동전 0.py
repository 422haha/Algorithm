import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
lst = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
lst.sort(reverse=True)
cnt = 0
for i in lst:
    coin = 0
    if k // i >= 1:
        coin = k // i
        k -= coin * i
        cnt += coin
print(cnt)