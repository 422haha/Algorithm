for _ in range(int(input())):
    s = input()
    mid = len(s)//2
    if s[mid-1] == s[mid]:
        print('Do-it')
    else:
        print('Do-it-Not')
