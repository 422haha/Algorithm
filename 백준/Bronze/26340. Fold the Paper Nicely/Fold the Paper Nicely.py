for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(f'Data set: {a} {b} {c}')
    for i in range(c):
        if a > b:
            a = a//2
        else:
            b = b//2
    if a < b:
        a, b = b, a
    print(a, b)
    print()