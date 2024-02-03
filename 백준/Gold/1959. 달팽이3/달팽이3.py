import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

# 변환점
if n > m:
    change_dr = 2*m-1
else:
    change_dr = 2*n-2
# 마지막 지점
if n == m:
    if n % 2 == 0:
        ri = n // 2 + 1
        rj = n // 2
    else:
        ri = n // 2 + 1
        rj = n // 2 + 1
elif min(n, m) % 2 == 0:
    ri = min(n, m) // 2 + 1
    rj = min(n, m) // 2
elif n > m:
    if m % 2 == 0:
        ri = m // 2 + 1
        rj = m // 2
    else:
        ri = n - m // 2
        rj = m // 2 + 1
else:
    if n % 2 == 0:
        ri = n // 2 + 1
        rj = n // 2
    else:
        ri = n // 2 + 1
        rj = m - n // 2

print(change_dr)
print(ri, rj)