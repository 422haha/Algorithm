import sys

a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())
a3, b3 = map(int, sys.stdin.readline().split())

if a1 == a2:
    if b1 ==b3:
        print(a3, b2)
    else:
        print(a3, b1)
elif a1 == a3:
    if b1 == b2:
        print(a2, b3)
    else:
        print(a2, b1)
else:# a2 a3
    if b1 == b2:
        print(a1, b3)
    else:
        print(a1, b2)