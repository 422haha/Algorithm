for i in range(int(input())):
    res = 0
    for j in range(int(input())):
        _, a, b = input().split()
        res += float(a)*float(b)
    print(f'${res:.2f}')