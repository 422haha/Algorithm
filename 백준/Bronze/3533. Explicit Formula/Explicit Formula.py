import sys
import math

n = 10-sum(list(map(int, sys.stdin.readline().split())))
c2 = math.comb(10, 2)-math.comb(n, 2)
c3 = math.comb(10, 3)-math.comb(n, 3)

print((c2+c3)%2)