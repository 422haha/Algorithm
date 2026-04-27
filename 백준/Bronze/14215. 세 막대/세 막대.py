import sys
a, b, c = map(int, sys.stdin.readline().split())
lst = [a, b, c]

if 2*max(lst) < sum(lst):
    print(a + b + c)
else:
    print(2*sum(lst)-2*max(lst)-1)