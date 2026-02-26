for _ in range(int(input())):
    res = 0
    for i in range(int(input())):
        tmp = list(map(int, input().split()))
        if max(tmp) >= 0:
            res += max(tmp)
    print(res)