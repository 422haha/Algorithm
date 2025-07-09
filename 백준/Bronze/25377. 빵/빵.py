lst = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    if b >= a:
        lst.append(b)

print(min(lst) if lst else -1)