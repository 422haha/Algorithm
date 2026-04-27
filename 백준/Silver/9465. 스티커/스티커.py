import sys

t = int(sys.stdin.readline().rstrip())
for tc in range(1, t+1):
    n = int(sys.stdin.readline().rstrip())
    arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(2)]
    if n > 1:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]
    for i in range(2, n):
        arr[0][i] += max(arr[1][i-1], arr[1][i-2])
        arr[1][i] += max(arr[0][i-1], arr[0][i-2])
    print(max(arr[0][n-1], arr[1][n-1]))