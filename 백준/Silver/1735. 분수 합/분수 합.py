import sys

def gcd(num1, num2):
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1


a1, b1 = map(int, sys.stdin.readline().rstrip().split())
a2, b2 = map(int, sys.stdin.readline().rstrip().split())
nu = a1*b2 + a2*b1
deno = b1*b2
ab = gcd(nu, deno)
print(nu//ab, deno//ab)