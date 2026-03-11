ans = [(i-1)%5+1 for i in range(1, 11)]
res = []
for i in range(int(input())):
    lst = list(map(int, input().split()))
    if ans == lst:
        res.append(i+1)
for i in res:
    print(i)