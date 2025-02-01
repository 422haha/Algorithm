res = 0

for _ in range(int(input())):
    a, d, g = map(int, input().split())
    res = max(((a==d+g)+1)*a*(d+g), res)

print(res)