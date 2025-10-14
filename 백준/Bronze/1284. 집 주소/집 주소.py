while True:
    n = int(input())
    if n == 0:
        break
    n = list(str(n))
    res = 0
    for i in n:
        if i == '1':
            res += 2
        elif i == '0':
            res += 4
        else:
            res += 3
    res += len(n)+1
    print(res)