n = int(input())
money = {136: 1000, 142: 5000, 148: 10000, 154: 50000}
res = 0

for _ in range(n):
    w, h = map(int, input().split())
    res += money[w]

print(res)