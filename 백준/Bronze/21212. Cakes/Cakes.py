res = 10001

for _ in range(int(input())):
    a, b = map(int, input().split())
    if res > b//a:
        res = b//a

print(res)