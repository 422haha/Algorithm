import sys
import math

n = int(sys.stdin.readline().rstrip())
res = 0

if int(math.sqrt(n)) ** 2 == n:
    print(-1)
else:
    for i in range(1, int(math.sqrt(n / 2)) + 1):
        j = n - i ** 2
        if int(math.sqrt(j)) ** 2 == j:
            res += 1
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            a, b = i, n // i
            if (a + b) % 2 == 0 and a != b:
                res += 1
    print(res)