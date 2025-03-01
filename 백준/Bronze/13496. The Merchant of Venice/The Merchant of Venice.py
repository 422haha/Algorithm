for k in range(int(input())):
    if k != 0:
        print()
    n, s, d = map(int, input().split())
    res=0
    for _ in range(n):
        di, v = map(int, input().split())
        if s*d >= di:
            res +=v
    print(f'Data Set {k+1}:')
    print(res)