import sys
import math

n, a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
ans = 10**18


if b * c > d * a:   # b//a, d//c 비교
    good = [c, d]
    bad = [a, b]
else:
    good = [a, b]
    bad = [c, d]

for i in range(good[0]):
    temp = n - i * bad[0]
    if temp < 0:
        j = 0
    else:
        j = math.ceil(temp / good[0])
    ans = min(ans, i * bad[1] + j * good[1])

print(ans)