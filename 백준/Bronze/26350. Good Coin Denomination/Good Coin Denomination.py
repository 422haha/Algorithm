for _ in range(int(input())):
    flag = True
    a, *lst = map(int, input().split())
    print("Denominations:", *lst)
    for i in range(1, len(lst)):
        if lst[i-1]*2 > lst[i]:
            flag = False
    if flag:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")
    print()