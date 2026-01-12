ans = input()
for _ in range(int(input())):
    a, b = 0, 0
    num = input()
    for i in range(len(ans)):
        if ans[i] == num[i]:
            b += 1
        if num[i] in ans:
            a += 1
    print(a, b)