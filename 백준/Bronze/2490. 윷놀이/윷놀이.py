for _ in range(3):
    lst = list(map(int, input().split()))
    back = lst.count(0)
    if back == 1:
        print('A')
    elif back == 2:
        print('B')
    elif back == 3:
        print('C')
    elif back == 4:
        print('D')
    elif back == 0:
        print('E')