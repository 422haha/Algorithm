import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

res = arr[n-1][0]*arr[0][1] - arr[n-1][1]*arr[0][0]         # 넓이
for i in range(n-1):
    res += arr[i][0]*arr[i+1][1] - arr[i][1]*arr[i+1][0]
res = round(abs(res/2), 1)                                  # 소수점 아래 둘째 자리 반올림

print(res)