import sys
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

n = int(sys.stdin.readline().rstrip())
num = int(sys.stdin.readline().rstrip())
arr = [[0]*n for _ in range(n)]
ni, nj, dr = 0, 0, 0
cnt = n**2
while cnt > 0:
    if 0 <= ni+di[dr] < n and 0 <= nj+dj[dr] < n and arr[ni+di[dr]][nj+dj[dr]] == 0:
        arr[ni][nj] = cnt
        if cnt == num:
            num_i = ni
            num_j = nj
        ni += di[dr]
        nj += dj[dr]
        cnt -= 1
    else:
        dr = (dr+1) % 4
    if cnt == 1:
        arr[ni][nj] = cnt
        if cnt == num:
            num_i = ni
            num_j = nj
        break

for lst in arr:
    print(*lst)
print(num_i+1, num_j+1)