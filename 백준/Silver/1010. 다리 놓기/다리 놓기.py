import sys

def factorial(num):
    if num == 0:
        return 1
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res


t = int(sys.stdin.readline().rstrip())
for tc in range(1, t+1):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    mcn = factorial(m)//(factorial(m-n)*factorial(n))
    print(mcn)