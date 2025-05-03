n = int(input())
lst = list(map(int, input().split()))

temp = 0
res = 0

for i in lst:
    if i == 1:
        temp += 1
    else:
        temp -= 1
    res += temp

print(res)
