import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    lst = [a, b, c]
    if a + b + c == 0:
        break
    if 2*max(lst) >= sum(lst):
        print('Invalid')
    elif a == b and b == c:
        print('Equilateral')
    elif a==b or b==c or a==c:
        print('Isosceles')
    else:
        print('Scalene')