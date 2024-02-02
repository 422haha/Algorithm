import sys

t = int(sys.stdin.readline().rstrip())
def gcd(num1, num2):
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1

for tc in range(1, t+1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    res = gcd(a, b)
    print(res*(a//res)*(b//res))