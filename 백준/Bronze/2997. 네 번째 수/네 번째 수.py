lst = sorted(list(map(int, input().split())))

if lst[1]-lst[0] == lst[2]-lst[1]:
    print(lst[2]*2-lst[1])
elif lst[1]-lst[0] > lst[2]-lst[1]:
    print(lst[1]*2-lst[2])
else:
    print(lst[1]*2-lst[0])