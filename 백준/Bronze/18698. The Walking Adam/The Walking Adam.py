for _ in range(int(input())):
    s = input()
    if 'D' in s:
        print(s.find('D'))
    else:
        print(len(s))