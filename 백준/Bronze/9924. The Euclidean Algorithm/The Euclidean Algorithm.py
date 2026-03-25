a, b = map(int, input().split())
c = 0
while b:
    a, b, c = b, a%b, c+a//b
print(c-1)