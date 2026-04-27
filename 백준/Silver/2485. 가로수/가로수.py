import sys
def gcd(num1, num2):
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1


n = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline().rstrip()))

dif = []
for i in range(len(lst)-1):
    dif.append(lst[i+1]-lst[i])

g = dif[0]
for i in range(1, len(dif)):
    g = gcd(g, dif[i])

res = 0
for i in dif:
    res += i//g-1

print(res)