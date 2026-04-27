import sys
def gcd(num1, num2):
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1

n, m = map(int, sys.stdin.readline().rstrip().split())
g = gcd(n, m)
print(g)
print((n//g)*(m//g)*g)