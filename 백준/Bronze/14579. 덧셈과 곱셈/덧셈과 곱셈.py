a, b = map(int, input().split())
res = 1

for i in range(a, b+1):
    res *= i*(i+1)//2

print(res%14579)