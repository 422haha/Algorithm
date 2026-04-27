import sys


def check(a, b, c):
    h1 = (a**2-c**2)**0.5
    h2 = (b**2-c**2)**0.5
    return h1*h2/(h1+h2)


x, y, c = map(float, sys.stdin.readline().rstrip().split())
s, e = 0, min(x, y)
res = 0

while e-s > 0.000001:   # 0으로 하면 x
    m = (s+e)/2
    if check(x, y, m) >= c:
        res = m
        s = m
    else:
        e = m
print(f'{res:0.3f}')