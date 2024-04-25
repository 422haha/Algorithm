import sys
from collections import deque
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def find(color):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == color:
                return i, j


def move(pos, d):
    x, y = pos
    cnt = 0
    while arr[x+di[d]][y+dj[d]] != '#' and arr[x][y] != 'O':
        x += di[d]
        y += dj[d]
        cnt += 1
    return (x, y), cnt


def bfs(red, blue):
    global res
    dq = deque()
    dq.append((red, blue))
    visited = set()
    visited.add((red, blue))
    cnt = 1
    while dq:
        for _ in range(len(dq)):
            red, blue = dq.popleft()
            if cnt > 10:
                return
            for d in range(4):
                new_red, rcnt = move(red, d)
                new_blue, bcnt = move(blue, d)
                if new_blue == goal:
                    continue
                if new_red == goal:
                    res = cnt
                    return
                if new_red == new_blue:
                    if rcnt > bcnt:
                        new_red = (new_red[0] - di[d], new_red[1] - dj[d])
                    else:
                        new_blue = (new_blue[0] - di[d], new_blue[1] - dj[d])
                if (new_red, new_blue) not in visited:
                    dq.append((new_red, new_blue))
                    visited.add((new_red, new_blue))
        cnt += 1


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

red = find('R')
blue = find('B')
goal = find('O')

res = -1
bfs(red, blue)
print(res)