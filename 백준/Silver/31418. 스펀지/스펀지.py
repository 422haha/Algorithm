import sys

w, h, k, t = map(int, sys.stdin.readline().rstrip().split())

mod = 998244353
res = 1

idx = 4
for i in range(k):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    idx += 2

    res *= (min(w, x+t) - max(1, x-t) + 1) % mod
    res %= mod
    res *= (min(h, y+t) - max(1, y-t) + 1) % mod
    res %= mod

print(res)