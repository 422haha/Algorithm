for _ in range(int(input())):
    n = int(input())
    lst = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            lst.append((i, j))
    lst = list(filter(lambda x: sum(x) == n, lst))
    print(f'Pairs for {n}: {", ".join([f"{t[0]} {t[1]}" for t in lst])}')