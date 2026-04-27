import sys

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(3)]

temp_l = arr[0][0]*arr[1][1] + arr[1][0]*arr[2][1] + arr[2][0]*arr[0][1]
temp_r = arr[0][1]*arr[1][0] + arr[1][1]*arr[2][0] + arr[2][1]*arr[0][0]

if temp_l > temp_r:     # 반시계 방향
    print(1)
elif temp_l < temp_r:   # 시계 방향
    print(-1)
elif temp_l == temp_r:  # 일직선
    print(0)