n, k = map(int, input().split())

res = 0
temp = 0

for _ in range(n):
    command = str(input().strip())

    if command == "ammo":
        res += k

    elif command == "save":
        temp = res

    elif command == "load":
        res = temp if temp is not None else 0

    elif command == "shoot":
        if res > 0:
            res -= 1

    print(res)
