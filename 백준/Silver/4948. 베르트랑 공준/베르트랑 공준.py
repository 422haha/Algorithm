import sys
import math
m = 123456
arr = [True for _ in range(2*m+1)]
arr[0], arr[1] = False, False
for i in range(2, math.isqrt(2*m)+1):
    j = 2
    while i*j <= 2*m:
        arr[i*j] = False
        j += 1

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if arr[i]:
            cnt += 1
    print(cnt)