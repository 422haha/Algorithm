n = int(input())
sa, sb = 0, 0

for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        sa += 1
    elif a < b:
        sb += 1

print(sa, sb)