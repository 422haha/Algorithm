n = int(input())
lst = [int(input()) for _ in range(n)]

missing = [i for i in range(1, lst[-1]+1) if i not in lst]

if missing:
    for num in missing:
        print(num)
else:
    print("good job")