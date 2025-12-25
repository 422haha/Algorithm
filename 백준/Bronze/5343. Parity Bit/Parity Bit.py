for _ in range(int(input())):
    s = input()
    res = 0
    for i in range(0, len(s), 8):
        temp = s[i:i+8]
        if temp[:7].count('1')%2 != int(temp[7]):
            res += 1
    print(res)