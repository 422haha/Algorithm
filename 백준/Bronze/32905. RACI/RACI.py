n, m = map(int, input().split())

for _ in range(n):
    r = input().split()
    if r.count('A') != 1:
        print("No")
        exit()
print("Yes")
