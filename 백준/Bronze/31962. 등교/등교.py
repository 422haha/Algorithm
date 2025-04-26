n, x = map(int, input().split())
latest = -1

for _ in range(n):
    s, t = map(int, input().split())
    if s+t <= x:
        latest = max(latest, s)

print(latest)