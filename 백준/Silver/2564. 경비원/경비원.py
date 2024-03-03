import sys


def distance(d, l):
    if d == x:
        return abs(l-y)
    elif d + x == 3:
        if (l + y + r) < (r + c + c - l - y):
            return l + y + r
        else:
            return r + c + c - l - y
    elif d + x == 7:
        if (l + y + c) < (r + r + c - l - y):
            return l + y + c
        else:
            return r + r + c - l - y
    else:
        if d + x == 4:
            return l + y
        elif d + x == 6:
            return r + c - y - l
        elif d == 1 and x == 4:
            return c - l + y
        elif x == 1 and d == 4:
            return c + l - y
        elif d == 2 and x == 3:
            return r + l - y
        else:
            return r - l + y


c, r = map(int, sys.stdin.readline().rstrip().split())
n = int(sys.stdin.readline())
lst = []

for i in range(n):
    d, l = map(int, sys.stdin.readline().rstrip().split())
    lst.append([d, l])

x, y = map(int, sys.stdin.readline().rstrip().split())

res = 0
for i in range(n):
    d, l = lst[i][0], lst[i][1]
    res += distance(d, l)

print(res)