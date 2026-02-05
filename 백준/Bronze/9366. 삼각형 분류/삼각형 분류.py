for i in range(int(input())):
    lst = sorted(list(map(int, input().split())))
    if lst[0]+lst[1] <= lst[2]:
        print(f"Case #{i+1}: invalid!")
    elif lst[0] == lst[2]:
        print(f"Case #{i+1}: equilateral")
    elif lst[1] in (lst[0], lst[2]):
        print(f"Case #{i+1}: isosceles")
    else:
        print(f"Case #{i+1}: scalene")