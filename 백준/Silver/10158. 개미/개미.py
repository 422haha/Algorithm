import sys

w, h = map(int, sys.stdin.readline().rstrip().split())
p, q = map(int, sys.stdin.readline().rstrip().split())
t = int(sys.stdin.readline())

p += t
q += t

p %= 2*w
q %= 2*h

if p > w:
    p = 2*w - p
if q > h:
    q = 2*h - q

print(p, q)