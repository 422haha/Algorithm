for _ in range(int(input())):
    s = input()
    res = 2015
    for c in set(s):
        res -= ord(c)
    print(res)