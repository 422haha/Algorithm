import sys


def ccw(p1, p2, p3):
    return p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])


points = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(3)]

if ccw(points[2], points[1], points[0]) > 0:
    points[2], points[0] = points[0], points[2]

area = abs(ccw(points[0], points[1], points[2]) / 2.0)
print("{:.1f}".format(area))

n = int(sys.stdin.readline().rstrip())
cnt = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    tmp = (x, y)
    if ccw(tmp, points[1], points[0]) > 0:
        continue
    if ccw(tmp, points[0], points[2]) > 0:
        continue
    if ccw(tmp, points[2], points[1]) > 0:
        continue
    cnt += 1

print(cnt)