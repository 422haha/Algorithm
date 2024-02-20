import sys

k = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(6)]
r = []
c = []
max_idx = 0

for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        r.append(arr[i][1])
    else:
        c.append(arr[i][1])
    if arr[max_idx][1] < arr[i][1]:
        max_idx = i

if max_idx == 0:
    if arr[5][1] < arr[1][1]:
        area_2 = arr[3][1] * arr[4][1]
    else:
        area_2 = arr[2][1] * arr[3][1]
elif max_idx == 1:
    if arr[0][1] < arr[2][1]:
        area_2 = arr[4][1] * arr[5][1]
    else:
        area_2 = arr[3][1] * arr[4][1]
elif max_idx == 2:
    if arr[1][1] < arr[3][1]:
        area_2 = arr[5][1] * arr[0][1]
    else:
        area_2 = arr[4][1] * arr[5][1]
elif max_idx == 3:
    if arr[2][1] < arr[4][1]:
        area_2 = arr[0][1] * arr[1][1]
    else:
        area_2 = arr[5][1] * arr[0][1]
elif max_idx == 4:
    if arr[3][1] < arr[5][1]:
        area_2 = arr[1][1] * arr[2][1]
    else:
        area_2 = arr[0][1] * arr[1][1]
elif max_idx == 5:
    if arr[4][1] < arr[0][1]:
        area_2 = arr[2][1] * arr[3][1]
    else:
        area_2 = arr[1][1] * arr[2][1]

area = max(r) * max(c)
res = (area-area_2) * k
print(res)