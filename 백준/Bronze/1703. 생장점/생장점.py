while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    cnt = 1
    for i in range(lst[0]):
        sf = lst[2*i+1]
        p = lst[2*i+2]
        cnt = cnt*sf-p
    print(cnt)