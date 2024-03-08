import sys


def ccw(a1, b1, a2, b2, a3, b3):
    temp = a1*b2 + a2*b3 + a3*b1
    temp -= b1*a2 + b2*a3 + b3*a1
    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0


x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().rstrip().split())

if (x1, y1) == (x3, y3) or (x1, y1) == (x4, y4) or (x2, y2) == (x3, y3) or (x2, y2) == (x4, y4):    # 두 선분이 한 점에서 만나면 1 출력 후 종료
    print(1)
    sys.exit(0)

l1 = ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4)  # 선분 l1과 x3, x4 ccw 곱
l2 = ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2)  # 선분 l2와 x1, x2 ccw 곱

if l1 == l2 == 0:
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        print(1)
        sys.exit(0)

elif l1 <= 0 and l2 <= 0:     # 곱이 둘 다 0 미만이면 교차함
    print(1)
    sys.exit(0)

print(0)