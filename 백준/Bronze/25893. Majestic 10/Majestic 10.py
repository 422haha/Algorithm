n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

for i in lst:
    print(*i)
    cnt = sum(1 for j in i if j >= 10)
    if cnt == 0:
        print("zilch")
    elif cnt == 1:
        print("double")
    elif cnt == 2:
        print("double-double")
    else:
        print("triple-double")
    print()