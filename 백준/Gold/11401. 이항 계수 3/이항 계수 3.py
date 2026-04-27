import sys


def factorial(num):
    res = 1
    for i in range(1, num+1):
        res = (res * i) % 1000000007  # 중간에 모듈러 연산 적용
    return res


n, k = map(int, sys.stdin.readline().rstrip().split())

# 이항 계수 계산
n_factorial = factorial(n)
nk_factorial = factorial(n-k)
k_factorial = factorial(k)

# 중간 결과에 모듈러 연산 적용
nck = (n_factorial * pow(nk_factorial * k_factorial, 1000000005, 1000000007)) % 1000000007

print(nck)