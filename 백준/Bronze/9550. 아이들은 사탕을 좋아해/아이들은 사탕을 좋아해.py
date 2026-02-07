for _ in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    res = 0
    for i in lst:
        res += i//k
    print(res)