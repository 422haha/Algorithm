for i in range(int(input())) :
    h = int(input())
    s = input()
    c = s.count('c')
    b = s.count('b')
    print('Data Set %d:'%(i+1))
    print(h+c-b)
    print()