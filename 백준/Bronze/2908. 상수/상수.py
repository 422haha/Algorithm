import sys
a, b = sys.stdin.readline().split()
rvs_a = int(a[::-1])
rvs_b = int(b[::-1])

if rvs_a > rvs_b:
    print(rvs_a)
else:
    print(rvs_b)