import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
lst.sort()
res = 2e9                       # |A[i]|이므로 *2

if n == 1:
    print(0)
    sys.exit(0)                 # 예외처리

i, j = 0, 1                     # 투포인터

while i < n and j < n:
    temp = lst[j] - lst[i]      # 두 수의 차
    if temp == m:
        print(m)
        sys.exit(0)
    elif temp > m:
        if res > temp:
            res = temp
        i += 1
    else:
        j += 1

print(res)