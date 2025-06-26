from math import gcd

n, a, b = map(int, input().split())
lcm = a*b//gcd(a, b)
fb = n//lcm
f = n//a-fb
b = n//b-fb
print(f, b, fb)