import sys

for tc in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, sys.stdin.readline().rstrip().split())
    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:
        print('d')
        continue
    elif p1 == x2 or p2 == x1:
        if q1 == y2 or q2 == y1:
            print('c')
            continue
        else:
            print('b')
            continue
    elif q1 == y2 or q2 == y1:
        print('b')
        continue
    else:
        print('a')