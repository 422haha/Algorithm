import sys

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
start = 1
end = k
res = 0

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in range(1, n + 1):
        temp += min(mid // i, n)
    if temp >= k:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)