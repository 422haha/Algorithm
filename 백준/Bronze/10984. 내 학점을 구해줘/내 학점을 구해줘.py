for i in range(int(input())):
    n = int(input())
    res = 0
    gpa = 0
    for j in range(n):
        c, g = input().split()
        res += int(c)
        gpa += float(g)*int(c)
    gpa /= res
    print(res, round(gpa, 1))