for _ in range(int(input())):
    lst = list(map(int, input().split()))
    print(*lst)
    print('both' if 18 in lst and 17 in lst else 'mack' if 18 in lst else 'zack' if 17 in lst else 'none')
    print()