for i in range(int(input())):
    lst = sorted(list(map(int, input().split())))
    print('Scenario #{}:'.format(i+1))
    if lst[0]**2+lst[1]**2 == lst[2]**2:  
        print("yes\n")
    else:
        print("no\n")