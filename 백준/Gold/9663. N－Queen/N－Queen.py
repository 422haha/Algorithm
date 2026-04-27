import sys


def check(r, c):
    if r == 0:
        return True
    for j in range(r):
        if arr[j] == c:
            return False
        if abs(arr[j] - arr[r]) == abs(j-r):
            return False
    return True


def n_queen(level):
    global cnt
    if level == n:
        cnt += 1
        return
    for i in range(n):
        arr[level] = i
        if check(level, i):
            n_queen(level+1)


n = int(sys.stdin.readline().rstrip())
arr = [0]*n
cnt = 0
n_queen(0)
print(cnt)