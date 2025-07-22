s = input()[:5]

res = 0
for _ in range(int(input())):
    if input()[:5] == s:
        res += 1

print(res)
