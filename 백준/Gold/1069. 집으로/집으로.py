import sys

x, y, d, t = map(int, sys.stdin.readline().rstrip().split())

temp = (x**2+y**2)**0.5
if temp >= d:   # 전체 거리가 d보다 큼
    res = min(temp, t*(temp//d)+temp%d, t*(temp//d+1))
else:           # 전체 거리가 d보다 작음
    res = min(temp, t+d-temp, 2*t)

print(res)