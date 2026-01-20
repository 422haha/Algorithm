for _ in range(int(input())):
    lst = list(map(int, input().split()))
    even = 0
    odd = 0
    for i in range(1, lst[0]+1):
        if lst[i]%2 == 0:
            even += lst[i]
        else:
            odd += lst[i]
    if even > odd:
        print('EVEN')
    elif even < odd:
        print('ODD')
    else:
        print('TIE')