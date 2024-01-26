n = int(input())
max_x = -10001
max_y = -10001
min_x = 10001
min_y = 10001

if n >= 2:
    for i in range(n):
        a, b = map(int, input().split())
        if a >= max_x:
            max_x = a
        if min_x >= a:
            min_x = a
        if b >= max_y:
            max_y = b
        if min_y >= b:
            min_y = b
    print((max_x-min_x)*(max_y-min_y))
else:
    a, b = map(int, input().split())
    print('0')