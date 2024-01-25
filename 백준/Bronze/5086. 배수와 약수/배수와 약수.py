while True:
    try:
        num_1, num_2 = map(int, input().split())
        if (num_2 // num_1 > 0) and (num_2 % num_1 == 0):
            print('factor')
        elif (num_1 // num_2 > 0) and (num_1 % num_2 == 0):
            print('multiple')
        else:
            print('neither')
    except:
        break