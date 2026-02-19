n = input()
res = 0

while len(n)>1:
    tmp = 1
    for i in range(len(n)):
        tmp *= int(n[i])
    n = list(str(tmp))
    res += 1

print(res)