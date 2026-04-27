import sys

def factorial(num):
    if num == 0:
        return 1
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res
n, k = map(int, sys.stdin.readline().rstrip().split())
nck = int(factorial(n)/(factorial(n-k)*factorial(k)))

print(nck)