for _ in range(int(input())):
    res = int(input())
    for _ in range(int(input())):
        q, p = map(int, input().split())
        res += q*p
    print(res)