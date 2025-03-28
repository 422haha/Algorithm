lst = [int(input()) for _ in range(5)]

for i in lst:
    if lst.count(i) % 2 == 1:
        print(i)
        break