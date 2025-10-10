while True:
    lst = list(map(int, input().split()))
    if sum(lst) == 0:
        break
    lst = sorted(lst)[1:-1]
    res = sum(lst)/4
    print(res if sum(lst)%4 else int(res))