import sys
from collections import defaultdict

t = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))

# A와 B의 부분합을 저장할 딕셔너리를 초기화
a_sum = defaultdict(int)
b_sum = defaultdict(int)

# 리스트 A의 모든 부분합을 계산하고 딕셔너리에 저장
for i in range(n):
    total = 0
    for j in range(i, n):
        total += a[j]
        a_sum[total] += 1

# 리스트 B의 모든 부분합을 계산하고 딕셔너리에 저장
for i in range(m):
    total = 0
    for j in range(i, m):
        total += b[j]
        b_sum[total] += 1

res = 0
# A의 부분합과 B의 부분합을 비교하여 원하는 합을 이루는 경우의 수 계산
for key in a_sum:
    if t - key in b_sum:
        res += a_sum[key] * b_sum[t - key]

print(res)