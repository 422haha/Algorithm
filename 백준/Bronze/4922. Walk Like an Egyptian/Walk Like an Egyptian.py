while True:
    n = int(input())
    if n == 0:
        break
    a = 1
    res = 0
    for i in range(n):
        if i == n-1:
           res += a//2
        else:
            res += a
            a += 2
    print(f"{n} => {res+1}")