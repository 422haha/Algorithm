import sys

# 입력을 받습니다.
n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

# 부분합 리스트와 나머지 카운트 리스트를 초기화합니다.
prefix_sums = [0] * n
remainders = [0] * m
result = 0

# 첫 번째 부분합을 계산합니다.
prefix_sums[0] = numbers[0]

# 부분합을 계산합니다.
for i in range(1, n):
    prefix_sums[i] = prefix_sums[i - 1] + numbers[i]

# 부분합을 m으로 나눈 나머지를 이용하여 결과를 계산합니다.
for i in range(n):
    remainder = prefix_sums[i] % m
    if remainder == 0:
        result += 1
    remainders[remainder] += 1

# 나머지 카운트 리스트를 이용하여 결과를 계산합니다.
for i in range(m):
    if remainders[i] > 1:
        result += (remainders[i] * (remainders[i] - 1) // 2)

# 결과를 출력합니다.
print(result)