lst = [input() for _ in range(int(input()))]
res = 0

for i in range(len(lst)):
    if lst[i] == input():
        res += 1

print(res)