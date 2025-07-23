res = 0
for _ in range(int(input())):
    q, y = map(float, input().split())
    res += q*y
print(f"{res:.3f}")