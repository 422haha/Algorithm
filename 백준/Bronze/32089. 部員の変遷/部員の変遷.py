while True:
    n = int(input())
    if n == 0:
        break
    lst = list(map(int,input().split()))
    res = 0
    for i in range(n-2):
        if sum(lst[i:i+3]) > res:
            res = sum(lst[i:i+3])
    print(res)