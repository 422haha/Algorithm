t = int(input())

for x in range(1, t+1):
    a, b = map(int, input().split())
    cnt = 0
    i = 1
    while True:
        cube = i*i*i
        if cube > b:
            break
        if cube >= a:
            cnt += 1
        i += 1
    print(f"Case #{x}: {cnt}")