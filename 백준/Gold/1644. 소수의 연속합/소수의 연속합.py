import sys
import math

n = int(sys.stdin.readline())
lst = list(range(n+1))
lst[1] = 0

for i in range(2, int(math.sqrt(n)+1)):
    if lst[i] == 0:
        continue
    j = 2
    while i*j <= n:                 # 에라토스테네스의 체
        lst[i*j] = 0
        j += 1

arr = []
for i in range(n+1):
    if lst[i] != 0:
        arr.append(lst[i])          # 소수만 arr 배열에  append

flag = 1
if len(arr) == 0:       # arr 배열이 비었을 때를 고려
    flag = 0
else:
    i, j = 0, 0         # 투 포인터
    temp = arr[0]
cnt = 0

while flag == 1:
    if temp >= n:
        if temp == n:
            cnt += 1
        temp -= arr[i]  # 부분합 갱신
        i += 1
    else:
        j += 1
        if j == len(arr):
            break
        temp += arr[j]  # 부분합 갱신

print(cnt)