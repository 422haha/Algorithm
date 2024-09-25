import math

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min(l-math.ceil(a/c), l-math.ceil(b/d)))