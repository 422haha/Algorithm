import sys
# 1 위, 2 아래, 3 오른쪽, 4 왼쪽
d = [0, -1, 1, 1, -1]
opp = [0, 2, 1, 4, 3]


def check(direction, length, speed, grid):
    length += speed * d[direction]
    length %= grid*2
    if length > grid:
        location = grid*2 - length
        direction = opp[direction]
    else:
        location = length
    return location, direction


r, c, m = map(int, sys.stdin.readline().rstrip().split())
r -= 1
c -= 1
arr = []
for _ in range(m):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    temp[0] -= 1
    temp[1] -= 1
    arr.append(temp)
now = 0
res = 0

while now <= c:
    arr.sort(key=lambda x: (x[1], x[0]))
    for i in range(len(arr)):
        if arr[i][1] == now:
            res += arr[i][4]
            arr.pop(i)
            break
    for i in range(len(arr)):
        if arr[i][3] == 1 or arr[i][3] == 2:
            row, direct = check(arr[i][3], arr[i][0], arr[i][2], r)
            arr[i][3] = direct
            arr[i][0] = row
        elif arr[i][3] == 3 or arr[i][3] == 4:
            col, direct = check(arr[i][3], arr[i][1], arr[i][2], c)
            arr[i][3] = direct
            arr[i][1] = col
    arr.sort(key=lambda x: (x[1], x[0], -x[4]))
    for i in range(len(arr)-1, 0, -1):
        if (arr[i][0], arr[i][1]) == (arr[i-1][0], arr[i-1][1]):
            arr.pop(i)
    now += 1

print(res)