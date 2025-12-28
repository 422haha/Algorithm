n = int(input())
sa, sb = 0, 0

for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        sa += a+b
    elif a == b:
        sa += a
        sb += b
    else:
        sb += a+b

print(sa, sb)