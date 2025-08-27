_ = int(input())
lst = list(map(int, input().split()))

res = 0
temp = 0

for i in lst:
    if i == 1:
        temp += 1
        res += temp
    else:
        temp = 0

print(res)