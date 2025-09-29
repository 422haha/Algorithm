lst = [int(input()) for _ in range(7)]
odds = []
res = 0

for i in lst:
    if i%2 != 0:
        odds.append(i)
        res += i

if not odds:
    print(-1)
else:
    print(res)
    print(min(odds))