import sys
def gcd(num1, num2):
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1
n = int(sys.stdin.readline())

for tc in range(1, 1+n):
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort(reverse=True)
    max_gcd = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if i != j:
                max_gcd = max(max_gcd, gcd(lst[i], lst[j]))
    print(max_gcd)